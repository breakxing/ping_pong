import sys
setting =   {'total_qbit':'26',
            'file_qbit':'3',
            'local_qbit':'12'}




#Fill what benchmark you want to run
benchmark = 'pp2_ori.c'
RDMA = 1
hf = 'ib_hf'




original_stdout = sys.stdout
with open('run.sh', 'w') as f:
    sys.stdout = f
    if(benchmark == 'pp2_ori.c'):
        print('mpicc pp2_ori.c -g -O3 -D_GNU_SOURCE -fopenmp -o pp2_ori')
        print('scp -q ./pp2_ori rdma2:/home/paslab/mpi_rdma/')
    elif(benchmark == 'pp2_quantum_pattern.c'):
        print('mpicc pp2_quantum_pattern.c -g -O3 -D_GNU_SOURCE -fopenmp -o pp2_quantum_pattern')
        print('scp -q ./pp2_quantum_pattern rdma2:/home/paslab/mpi_rdma/')
    else:
        sys.stdout = original_stdout
        print(f'No {benchmark}')
        exit(1)
    
    # Reset the standard output
    sys.stdout = original_stdout



