'''Page replacement algorithm, 
optimal replacement algorithm
'''


def opt_algo(seq):

    length = len(seq)
    replace_count = 0
    max_block_count = 3
    mem_blocks = []
    page_fault_interrupt = 0

    for item in seq:
        # check length
        if len(mem_blocks) < max_block_count:
            
            if item not in mem_blocks:
                mem_blocks.append(item)
                page_fault_interrupt += 1
        
        # mem block is full
        else:    
            # array left shift, and replace
            if item not in mem_blocks:
                replace_count += 1
                page_fault_interrupt += 1

                for i in range(len(mem_blocks) - 1):
                    mem_blocks[i] = mem_blocks[i + 1]
                mem_blocks[max_block_count - 1] = item
            
            # if in blocks, then swap the change position
            else:
                # if not the lastest viewd
                if i != seq[-1]:

                    for i in range(len(seq) - 1):
                        if mem_blocks[i] == item:
                            # swap, consider it as the lastest viewd
                            mem_blocks[i], mem_blocks[max_block_count - 1] = mem_blocks[max_block_count - 1], mem_blocks[i]
                
        
    _str = f'present of replacement: {replace_count / length}%, replacement count: {replace_count}, page fault interrupt: {page_fault_interrupt}'

    return _str


if __name__ == '__main__':
    seq = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1]
    print(opt_algo(seq))
