class MemoryManagerPaging:
    def __init__(self, total_memory, page_size):
        self.total_memory = total_memory
        self.page_size = page_size
        self.num_pages = total_memory // page_size
        self.memory = [None] * self.num_pages  # None indicates free page

    def allocate(self, process_id, process_size):
        num_pages_needed = -(-process_size // self.page_size)  # Ceiling division to get pages needed
        allocated_pages = []
        
        for i in range(self.num_pages):
            if len(allocated_pages) == num_pages_needed:
                break
            if self.memory[i] is None:  # Free page found
                self.memory[i] = process_id
                allocated_pages.append(i)

        if len(allocated_pages) == num_pages_needed:
            print(f"Process {process_id} allocated at pages {allocated_pages}.")
            return allocated_pages
        else:
            # Rollback if not enough pages are available
            for page in allocated_pages:
                self.memory[page] = None
            print(f"Not enough memory to allocate Process {process_id}.")
            return []

    def deallocate(self, process_id):
        for i in range(self.num_pages):
            if self.memory[i] == process_id:
                self.memory[i] = None
        print(f"Process {process_id} deallocated from memory.")

    def display_memory(self):
        print("Memory pages:", self.memory)

# Usage example
paging_manager = MemoryManagerPaging(total_memory=1024, page_size=128)
paging_manager.allocate("P1", 300)  # Process P1 needs 300KB
paging_manager.allocate("P2", 128)  # Process P2 needs 128KB
paging_manager.display_memory()
paging_manager.deallocate("P1")
paging_manager.display_memory()
