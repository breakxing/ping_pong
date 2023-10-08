#include <stdio.h>
#include <stdlib.h>
#include <omp.h>
#include <mpi.h>
#include <omp.h>
#include <time.h>
typedef double Type_t;
typedef unsigned long long ull;
typedef double Type_t;
typedef struct {
    Type_t real;
    Type_t imag;
} Type;
inline void _thread_read1_recv1_MPI(setStreamv2 *s,int member_th,int num_worker,ull stride);
int main(int argc, char** argv) {
    int rank, size;
    MPI_Status status;
    double start_time, end_time, total_time;
    int i, j;
    int provided;
    double total_time_all_thread;
    ull N = 35;
    ull mpi_seg = 1;
    ull chunk_seg = 12;
    ull file_seg = 5;
    ull num_thread = 1 << file_seg;
    N = N - mpi_seg;
    ull num_chunk = 1 << (N - file_seg - chunk_seg);
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
    omp_set_num_threads(num_thread);
    srand(time(NULL));
    #pragma omp parallel private(start_time, end_time, total_time,i, j)
    {
        int t = omp_get_thread_num();
        #pragma omp barrier
        // Perform ping-pong communication
        ull message_size = (1 << 12) * sizeof(Type);
        char* message = (char*)malloc(message_size);

        if (rank == 0) {
            // Process A sends message to Process B
            start_time = MPI_Wtime();
            for (i = 0; i < num_chunk; i++) {
                MPI_Send(message, message_size, MPI_CHAR, 1, t, MPI_COMM_WORLD);
                MPI_Recv(message, message_size, MPI_CHAR, 1, t, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
            }
            end_time = MPI_Wtime();
        } else if (rank == 1) {
            // Process B receives message from Process A and sends it back
            for (i = 0; i < num_chunk; i++) {
                MPI_Recv(message, message_size, MPI_CHAR, 0, t, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
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
                double startup_time = total_time_all_thread / (2 * num_chunk * num_thread);
                double bandwidth = (message_size * 1e-6) / startup_time;
                printf("Avg Total Time: %.6f seconds\n",total_time_all_thread / num_thread);
                printf("Message Size: %lld bytes\n", message_size);
                printf("Avg Startup Time: %.6f seconds\n", startup_time);
                printf("Avg Bandwidth: %.6f MB/s\n", bandwidth);
                printf("===========================================\n");
            }
        }
        #pragma omp barrier
        free(message);
        
    }
    

    MPI_Finalize();
    return 0;
}


inline void _thread_read1_recv1_MPI(setStreamv2 *s,int member_th,int num_worker,ull stride)
{
    MPI_Irecv(s->rd + (!member_th) * chunk_size, chunk_size, MPI_BYTE, s->partner_rank[0], s->id, MPI_COMM_WORLD,&s->request[!member_th]);
    if(num_worker == 2)
    {
        if(pread(s->fd[0], s->rd + (chunk_size << 1), chunk_size, s->fd_off[0] + (!member_th) * stride));
        MPI_Isend(s->rd + (chunk_size << 1), chunk_size, MPI_BYTE, s->partner_rank[0], s->id, MPI_COMM_WORLD,&s->request[2]);
    }
    if(pread(s->fd[0], s->rd + member_th * chunk_size, chunk_size, s->fd_off[0] + member_th * stride));
    MPI_Wait(&s->request[!member_th],MPI_STATUS_IGNORE);
    gate_func((Type *)s->rd);
    MPI_Isend(s->rd + (!member_th) * chunk_size, chunk_size, MPI_BYTE, s->partner_rank[0], s->id, MPI_COMM_WORLD,&s->request[!member_th]);
    if(pwrite(s->fd[0], s->rd + member_th * chunk_size, chunk_size, s->fd_off[0] + member_th * stride));
    if(num_worker == 2)
    {
        MPI_Recv(s->rd + (chunk_size << 1), chunk_size, MPI_BYTE, s->partner_rank[0], s->id, MPI_COMM_WORLD,MPI_STATUS_IGNORE);
        if(pwrite(s->fd[0], s->rd + (chunk_size << 1), chunk_size, s->fd_off[0] + (!member_th) * stride));
    }


}