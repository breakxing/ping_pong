#include <stdio.h>
#include <stdlib.h>
#include <omp.h>
#include <mpi.h>
#include <omp.h>
#include <time.h>
#include <string.h>
#include <math.h>
typedef struct setStreamv2 {
    int id;             // thread id
    unsigned int partner_rank[8];      // correspond rank for mpi
    void *rd;           // 指向buffer的位置
    MPI_Request request[15];
} setStreamv2;
setStreamv2 *thread_settings;
typedef double Type_t;
typedef unsigned long long ull;
typedef double Type_t;
typedef struct {
    Type_t real;
    Type_t imag;
} Type;
ull chunk_size;
ull buffer_size;
inline void _thread_read1_recv1_MPI(setStreamv2 *s,int member_th,int num_worker,ull stride);
int main(int argc, char** argv) {
    int rank, size;
    MPI_Status status;
    double start_time, end_time, total_time;
    int i, j;
    int provided;
    double total_time_all_thread;
    ull N = 30;
    ull mpi_seg = 1;
    ull chunk_seg = 12;
    chunk_size = (1 << chunk_seg) * sizeof(Type);
    ull file_seg = 3;
    ull num_thread = 1 << file_seg;
    N = N - mpi_seg;
    ull num_chunk = 1 << (N - file_seg - chunk_seg);
    thread_settings = (setStreamv2 *)malloc(num_thread * sizeof(setStreamv2));
    buffer_size = (num_thread * 15 * chunk_size);
    char *allrd = (char*)malloc(buffer_size);
    for(int i = 0;i < num_thread;i++)
    {
        thread_settings[i].rd = allrd + i * 15 * chunk_size;
    }

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
        setStreamv2 *s = &thread_settings[t];
        s->id = t;
        s->partner_rank[0] = !rank;
        #pragma omp barrier
        // Perform ping-pong communication
        if (rank == 0) {
            // Process A sends message to Process B
            start_time = MPI_Wtime();
            for (i = 0; i < num_chunk; i++) {
                _thread_read1_recv1_MPI(s,0,2,chunk_size);
            }
            end_time = MPI_Wtime();
        } else if (rank == 1) {
            // Process B receives message from Process A and sends it back
            for (i = 0; i < num_chunk; i++) {
                _thread_read1_recv1_MPI(s,1,2,chunk_size);
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
                printf("Message Size: %lld bytes\n", chunk_size);
                printf("Avg Total Time: %d us\n",(int)round(total_time_all_thread / num_thread * 1e6));
                printf("===========================================\n");
            }
        }
        #pragma omp barrier
        
    }
    
    free(thread_settings);
    free(allrd);
    MPI_Finalize();
    return 0;
}


inline void _thread_read1_recv1_MPI(setStreamv2 *s,int member_th,int num_worker,ull stride)
{
    MPI_Irecv(s->rd + (!member_th) * chunk_size, chunk_size, MPI_BYTE, s->partner_rank[0], s->id, MPI_COMM_WORLD,&s->request[!member_th]);
    if(num_worker == 2)
    {
        MPI_Isend(s->rd, chunk_size, MPI_BYTE, s->partner_rank[0], s->id, MPI_COMM_WORLD,&s->request[2]);
    }
    MPI_Wait(&s->request[!member_th],MPI_STATUS_IGNORE);
    MPI_Isend(s->rd + (!member_th) * chunk_size, chunk_size, MPI_BYTE, s->partner_rank[0], s->id, MPI_COMM_WORLD,&s->request[!member_th]);
    if(num_worker == 2)
    {
        MPI_Recv(s->rd + (chunk_size << 1), chunk_size, MPI_BYTE, s->partner_rank[0], s->id, MPI_COMM_WORLD,MPI_STATUS_IGNORE);
    }


}