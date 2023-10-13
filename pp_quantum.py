import sys
import os




#Fill what benchmark you want to run
benchmark = 'pp2_quantum_pattern.c'
USE_RDMA = 0
USE_RDMA_CARD = 0

RDMA_CARD1 = 'mlx5_1:1'
RDMA_CARD2 = 'mlx5_3:1'
RDMA_TCP_CARD1 = 'enp1s0f1np1'
RDMA_TCP_CARD2 = 'enp4s0f1np1'
MORMAL_TCP_CARD1 = 'eno2'
MORMAL_TCP_CARD2 = 'enp0s31f6'
hf = 'ib_hf'



original_stdout = sys.stdout
with open('run_quantum.sh', 'w') as f:
    sys.stdout = f
    if(benchmark == 'pp2_quantum_pattern.c'):
        print('mpicc pp2_quantum_pattern.c -g -O3 -D_GNU_SOURCE -fopenmp -o pp2_quantum_pattern -lm')
        print('scp -q ./pp2_quantum_pattern rdma2:/home/paslab/mpi_rdma/')
        if(USE_RDMA):
            if not USE_RDMA_CARD:
                sys.stdout = original_stdout
                print("RDMA Mode Need RDMA Network Card")
                exit(1)
            print(f'mpirun -x LSAN_OPTIONS -x UCX_NET_DEVICES={RDMA_CARD1},{RDMA_CARD2} -x LD_LIBRARY_PATH --hostfile ib_hf --bind-to none --map-by ppr:1:node ./pp2_quantum_pattern')
        else:
            if USE_RDMA_CARD:
                print(f'UCX_TLS=tcp mpirun -x UCX_NET_DEVICES={RDMA_TCP_CARD1},{RDMA_TCP_CARD2} -x LD_LIBRARY_PATH --hostfile ib_hf --bind-to none --map-by ppr:1:node ./pp2_quantum_pattern')
            else:
                print(f'mpirun -x UCX_NET_DEVICES={MORMAL_TCP_CARD1},{MORMAL_TCP_CARD2}  -x LD_LIBRARY_PATH --hostfile ib_hf --bind-to none --map-by ppr:1:node ./pp2_quantum_pattern')
    else:
        sys.stdout = original_stdout
        print(f'No {benchmark}')
        exit(1)
    
    # Reset the standard output
    sys.stdout = original_stdout
os.system(f'bash ./run_quantum.sh')



