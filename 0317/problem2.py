'''
5
5 1
7 2 5 8
4 7 6 6
4 4 3 3
0 1 3 3
1 0 4 2
5 4
5 6 4 4
8 3 6 4
1 4 2 2
1 8 2 11
4 9 3 8
10 5
12 2 10 1
5 0 4 5
3 10 5 8
1 0 0 1
6 10 7 8
0 2 1 0
6 5 1 6
7 8 6 6
4 10 6 11
4 4 7 3
30 0
102 132 11 76
8 97 107 23
36 99 74 158
92 72 31 58
86 50 122 37
97 78 159 27
98 157 13 100
27 36 4 130
3 9 18 102
69 69 152 123
86 103 98 29
54 53 151 5
1 107 12 80
95 159 5 65
48 56 4 126
1 95 44 83
94 98 130 88
97 186 72 89
37 88 85 50
111 36 22 104
71 58 34 11
70 109 24 91
93 86 129 96
107 90 30 149
95 158 64 82
38 13 58 56
99 99 142 128
138 76 68 127
101 92 30 182
102 85 56 149
50 19
193 32 227 173
271 237 90 151
264 127 151 300
100 148 183 195
149 157 283 297
258 291 42 205
260 275 262 119
281 268 294 93
32 291 23 295
135 252 6 249
5 256 83 162
58 280 295 198
126 75 153 85
167 147 169 70
300 200 152 161
175 277 231 276
195 233 108 14
265 193 172 232
176 127 26 57
281 235 223 124
9 111 251 9
238 136 161 219
101 49 80 234
155 143 285 212
142 223 58 283
264 300 217 211
94 271 27 128
191 145 169 258
147 94 196 235
139 262 117 279
264 205 230 296
170 170 258 18
259 218 245 262
287 136 283 1
96 240 154 237
269 278 275 247
297 218 293 169
236 110 286 117
19 300 174 133
258 298 285 235
162 300 229 13
42 231 268 195
288 131 258 101
282 211 280 151
279 145 271 147
273 274 191 299
179 142 48 271
49 294 22 257
132 187 75 184
159 249 163 147

'''
from itertools import combinations
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    tumors = []
    for i in range(len(arr)):
        if arr[i][0] > arr[i][2]:
            x = arr[i][2]
        else:
            x = arr[i][0]
        if arr[i][1] > arr[i][3]:
            y = arr[i][3]
        else:
            y = arr[i][1]
        x_len = abs(arr[i][0] - arr[i][2])
        y_len = abs(arr[i][1] - arr[i][3])
        #print(x, y, x_len, y_len)
        tumors.append([x, x+x_len, y, y+y_len])

    tumor_selected = N - M
    cases = list(combinations(tumors, tumor_selected))
    result = 999999
    for case in cases:
        min_x = sorted(case, key=lambda case:case[0])[0][0]
        max_x = sorted(case, key=lambda case:case[1])[-1][1]
        min_y = sorted(case, key=lambda case: case[2])[0][2]
        max_y = sorted(case, key=lambda case: case[3])[-1][3]
        row = max_x - min_x
        axis = max_y - min_y
        K = max(row, axis)
        if K < result:
            result = K
    print('#{} {}'.format(tc, result))
