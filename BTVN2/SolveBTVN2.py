# Đề bài: 
# Bạn đang đứng ở góc trên bên trái của một lưới kích thước m x n (m, n Khác 0), trong đó mỗi ô có một giá trị 
# nguyên dương, biểu thị chi phí để đi từ ô đó đến ô đích ở góc dưới bên phải của lưới. Bạn chỉ 
# có thể đi xuống hoặc sang trái. Hãy tìm đường đi từ ô đầu tiên đến ô đích sao cho tổng chi phí
# là nhỏ nhất và xuất ra màn hình đường đi mà bạn tìm được
m, n = map(int, input().split())
grid = []
for i in range(m):
    row = list(map(int, input().split()))
    grid.append(row)

def shortest_path(grid, m, n):
    # Chiều dài và chiều rộng của lưới
    # Tạo bảng lưu trữ độ dài đường đi ngắn nhất
    dp = [[0] * n for _ in range(m)]
    # Tính độ dài đường đi ngắn nhất từ góc trên bên trái đến mỗi ô
    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0:
                dp[i][j] = grid[i][j]
            elif i == 0:
                dp[i][j] = dp[i][j-1] + grid[i][j]
            elif j == 0:
                dp[i][j] = dp[i-1][j] + grid[i][j]
            else:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
    # Trả về độ dài đường đi ngắn nhất từ góc trên bên trái đến góc dưới bên phải
    return dp[m-1][n-1], dp

def path(dp, grid, m, n):
    # Tìm đường đi ngắn nhất từ góc trên bên trái đến góc dưới bên phải
    path_dp = []
    i = m - 1
    j = n - 1
    path_dp.append(grid[i][j])
    while i != 0 or j != 0:
        if i == 0:
            j -= 1
        elif j == 0:
            i -= 1
        elif dp[i-1][j] <= dp[i][j-1]:
            i -= 1
        else:
            j -= 1
        path_dp.append(grid[i][j])
    return path_dp[::-1]

if m==0 or n==0:
    exit()
else:
    dis, dp = shortest_path(grid, m, n)
    dp_t = path(dp,grid, m, n)

    print(dis)
    print(*dp_t)
