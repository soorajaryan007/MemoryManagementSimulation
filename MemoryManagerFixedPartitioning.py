class MemoryManagerFixedPartitioning:
    def __init__(self, total_memory, partition_size):
        self.total_memory = total_memory
        self.partition_size = partition_size
        self.num_partitions = total_memory // partition_size
        self.memory = [None] * self.num_partitions  # None indicates free partition

    def allocate(self, process_id):
        for i in range(self.num_partitions):
            if self.memory[i] is None:  # Check for a free partition
                self.memory[i] = process_id
                print(f"Process {process_id} allocated at partition {i}.")
                return i
        print(f"No free partition available for Process {process_id}.")
        return -1

    def deallocate(self, process_id):
        for i in range(self.num_partitions):
            if self.memory[i] == process_id:
                self.memory[i] = None
                print(f"Process {process_id} deallocated from partition {i}.")
                return
        print(f"Process {process_id} not found in memory.")

    def display_memory(self):
        print("Memory partitions:", self.memory)

# Usage example
fixed_partition_manager = MemoryManagerFixedPartitioning(total_memory=1024, partition_size=256)
fixed_partition_manager.allocate("P1")
fixed_partition_manager.allocate("P2")
fixed_partition_manager.display_memory()
fixed_partition_manager.deallocate("P1")
fixed_partition_manager.display_memory()
