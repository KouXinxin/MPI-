from mpi4py import MPI
print("hello world'', end = ",")
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
print("my rank is: %d" % rank)
