## Project 3 - Magical Eggs and Floors
### 10/22/2023

### Notes on Project 3:

* Source: https://www.youtube.com/watch?v=S49zeUjeUL0

* Some observations for code, not very consistent:

```
e = 1, f = 5 | Time: 162.1114 | Min Attempts Req: 5
e = 5, f = 25 | Time: 248.711 | Min Attempts Req: 5
e = 10, f = 50 | Time: 202.9419 | Min Attempts Req: 6
e = 15, f = 75 | Time: 243.5684 | Min Attempts Req: 7
e = 20, f = 100 | Time: 193.3445 | Min Attempts Req: 7
e = 25, f = 125 | Time: 230.3827 | Min Attempts Req: 7
e = 30, f = 150 | Time: 175.9811 | Min Attempts Req: 8
```

* It seems we cannot try for too much big values, since it results in `RecursionError: maximum recursion depth exceeded in comparison` issue, for the above code. Maximum I tried was `e = 150`, `f = 750`.

---