def rolling_dice(pip=6, repeat=1):
    for r in range(1, repeat+1):
        n=random.randint(1,pip)
        print(pip,
              "면 주사위 굴린 결과", r, ":", n)


