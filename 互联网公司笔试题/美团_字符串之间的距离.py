"""
����������ͬ���ȵ����ַ� a �� b ���ɵ��ַ������������ǵľ���Ϊ��Ӧλ�ò�ͬ���ַ���������
�紮��aab���봮��aba���ľ���Ϊ 2������ba���봮��aa���ľ���Ϊ 1������baa���ʹ���baa���ľ���Ϊ 0��
������������ַ��� S �� T������ S �ĳ��Ȳ�С�� T �ĳ��ȡ�������|S|���� S �ĳ��ȣ�|T|���� T �ĳ��ȣ�
��ô�� S ��һ����|S|-|T|+1 ���� T ������ͬ���Ӵ�����������Ҫ���� T ������Щ|S|-|T|+1 ���Ӵ��ľ���ĺ͡�
˼·��abbaabbaabba �� abba���Ƚϳ���ʱ
s: abbaabbaabba
t: abba
    abba
     abba
      abba
       abba
        abba
         abba
          abba
           abba
���Կ�������s������,�ӵ�3����ʼ����������3��֮�䣬�����ַ�����t�е�ÿ���ַ����˱Ƚϣ�
��ǰ��i�����ǱȽ�s�е�i���ַ���t��ǰ��i���ַ�
����i�����ǱȽ�s�еĵ�i���ַ���t�ĺ���i���ַ�
���Ǳ��뿼���������
"""
from collections import Counter
def get_count(char, string):
    d = Counter(string)
    return len(string) - d.get(char, 0)

def get_distance(s, t):
    len_s = len(s)
    len_t = len(t)

    start = len_t - 1
    end = len_s - len_t + 1
    count = 0
    # ���start��endС
    if start < end:
        # �Ƚ����
        for i in range(0, start):
            count += get_count(s[i], t[:i+1])
        # �Ƚ��ұ�
        for i in range(end, len_s):
            count += get_count(s[i], t[i-len_s+len_t:])
        # �Ƚ��м�
        for i in range(start, end):
            count += get_count(s[i], t)
            
    # ���endС�ڵ���start
    elif end <= start:
        # �Ƚ����
        for i in range(0, end):
            count += get_count(s[i], t[:i+1])
        # �Ƚ��ұ�
        for i in range(start, len_s):
            count += get_count(s[i], t[i-len_s+len_t:])
        # �Ƚ��м�
        for i in range(end, start):
            count += get_count(s[i], t[i-len_s+len_t:i+1])
    return count

if __name__ == "__main__":
    s = "aabaaabaaaba"
    t = "abaaaaa"
    print(get_distance(s, t))