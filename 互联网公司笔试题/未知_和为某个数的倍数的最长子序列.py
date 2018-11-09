"""
 �����������������Ԫ����ɵ������г�Ϊ�����е��Ӵ���
���ڸ���һ������P��һ������K��ѯ��Ԫ�غ���K�ı������Ӵ�����󳤶ȡ�
�������С�1,2,3,4,5������������KΪ5�����������������Ӵ�Ϊ{5},{2,3},{1,2,3,4},{1,2,3,4,5}
��ô�𰸾���5
���룺��һ�к�һ������N,�ڶ��а���N�������������а���һ������K��
"""
def get_max_len(arr, n, k):
    dp = [[0 for i in range(n)] for j in range(n)]

    for j in range(n):
        dp[n-1][0] += arr[j]

    if dp[n-1][0] % k == 0:
        return n

    for i in range(n-2, -1, -1):
        for j in range(n-i):
            if j == 0:
                dp[i][j] = dp[i+1][j] - arr[i+1]
            else:
                dp[i][j] = dp[i+1][j-1] - arr[j-1]
            if dp[i][j] % 5 == 0:
                return i+1
    return 0

if __name__ == '__main__':
    arr = [1, 2]
    n = len(arr)
    k = 5
    print(get_max_len(arr, n, k))