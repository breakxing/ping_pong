#include <stdio.h>
#include <stdlib.h>
#include <omp.h>
#include <mpi.h>
#include <omp.h>
#include <time.h>
#include <math.h>
#define NUM_MESSAGES 1000
double total_time_all_thread;
int main(int argc, char** argv) {
    int rank, size;
    MPI_Status status;
    double start_time, end_time, total_time;
    int message_sizes[25];
    int i, j, size_idx;
    int provided;
    MPI_Init_thread(NULL, NULL,MPI_THREAD_MULTIPLE,&provided);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    if (size != 2) {
        if (rank == 0) {
            printf("This program requires exactly 2 processes.\n");
        }
        MPI_Finalize();
        return 0;
    }
    if(rank == 0)
    {
        printf("Message_Size\tStartup_Time(us)\tBandwidth\n");
    }
    for (i = 0; i < 25; i++) {
        message_sizes[i] = 1;
        for (j = 0; j < i; j++){
            message_sizes[i] *= 2;
        }
    }


    int num_thread = omp_get_max_threads();
    omp_set_num_threads(num_thread);
    srand(time(NULL));
    #pragma omp parallel private(start_time, end_time, total_time,i, j,size_idx)
    {
        int t = omp_get_thread_num();
        
        for (size_idx = 0; size_idx < 25; size_idx++) {
            int message_size = message_sizes[size_idx];
            char* message = (char*)malloc(message_size);
            #pragma omp barrier
            if(t == 0)
                MPI_Barrier(MPI_COMM_WORLD);
            #pragma omp barrier
            
            if (rank == 0) {
                // Process A sends message to Process B
                start_time = MPI_Wtime();
                for (i = 0; i < NUM_MESSAGES; i++) {
                    MPI_Send(message, message_size, MPI_CHAR, 1, t, MPI_COMM_WORLD);
                    MPI_Recv(message, message_size, MPI_CHAR, 1, t, MPI_COMM_WORLD, &status);
                }
                end_time = MPI_Wtime();
            } else if (rank == 1) {
                // Process B receives message from Process A and sends it back
                for (i = 0; i < NUM_MESSAGES; i++) {
                    MPI_Recv(message, message_size, MPI_CHAR, 0, t, MPI_COMM_WORLD, &status);
                    MPI_Send(message, message_size, MPI_CHAR, 0, t, MPI_COMM_WORLD);
                }
            }

            total_time = end_time - start_time;
            if(t == 0 && rank == 0)
            {
                total_time_all_thread = 0;
            }
            #pragma omp barrier
            if (rank == 0) {
                #pragma omp critical
                {
                    total_time_all_thread += total_time;
                }
                #pragma omp barrier
                if(t == 0)
                {
                    double startup_time = total_time_all_thread / (2 * NUM_MESSAGES * num_thread);
                    double bandwidth = (message_size * 1e-6) / startup_time * num_thread;
                    double mes_size_log = log(message_size) / log(2);
                    if(mes_size_log >= 10)
                    {
                        printf("%-12d\t%-18d\t%-18d\n", (int)mes_size_log, (int)(startup_time * 1e6), (int)round(bandwidth));
                    }
                    // printf("Message Size: %d bytes\n", message_size);
                    // printf("Startup Time: %.6f seconds\n", startup_time);
                    // printf("Bandwidth: %.6f MB/s\n", bandwidth);
                    // printf("===========================================\n");
                }
            }

            free(message);
        }
    }


    // Perform ping-pong communication


    MPI_Finalize();
    return 0;
}