import queue
from Model import Direction


class Search:

    def __init__(self):
        pass

    def encode(self, row, col, world_map):
        return row * world_map.column_num + col
        pass

    def decode(self, num, world_map):
        return int(num / world_map.column_num), num % world_map.row_num
        pass

    def search(self, hero, world_map, row, col):
        q = queue.Queue()
        visited = [0] * world_map.column_num * world_map.row_num

        my_row = hero.current_cell.row
        my_col = hero.current_cell.column

        this_code = self.encode(my_row, my_col, world_map)
        q.put(this_code)
        visited[this_code] = -1

        while True:
            code = q.get()
            crow, ccol = self.decode(code, world_map)

            if crow == row and ccol == col:
                break

            arr = [[crow-1, ccol], [crow, ccol-1], [crow+1, ccol], [crow, ccol+1]]

            for i in range(4):
                x = arr[i][0]
                y = arr[i][1]
                if x < 0 or y < 0 or x >= world_map.row_num or y >= world_map.column_num:
                    continue

                cell_code = self.encode(x, y, world_map)

                if world_map.get_cell(x, y).is_wall or visited[cell_code] != 0:
                    continue

                visited[cell_code] = code
                q.put(cell_code)

        parent = code

        while visited[parent] != -1:
            code = parent
            # print(code, end=' ')
            parent = visited[parent]

        ncrow, nccol = self.decode(code, world_map)

        if ncrow < my_row:
            return Direction.UP
        if ncrow > my_row:
            return Direction.DOWN
        if nccol < my_col:
            return Direction.LEFT
        if nccol > my_col:
            return Direction.RIGHT
        return None


