'''Page replacement algorithm, FIFO algorithm
'''

def fifo(seq):

    page_fault_interrupt = 0
    max_queue_count = 3
    queue_list = []

    _str = ''

    for item in seq:
        if len(queue_list) < max_queue_count:
        
            if item not in seq:
                queue_list.append(item)
            page_fault_interrupt += 1
        
        else:
            if item not in seq:
                page_fault_interrupt += 1
            else:
                pass

            _str += 'current queue:\n'
            for ele in queue_list:
                _str += f'{ele}<-'
            _str += '\n'
            
            # array left shift
            for i in range(len(queue_list) - 1):
                queue_list[i] = queue_list[i + 1]
            queue_list[max_queue_count - 1] = item
            
            

    _str += f'page int: {page_fault_interrupt}'
    print(_str)


if __name__ == '__main__':
    seq = (3, 2, 1, 0, 3, 2, 4, 3, 2, 1, 0, 4)
    fifo(seq)
