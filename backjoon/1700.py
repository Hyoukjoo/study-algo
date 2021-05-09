n, k = map(int, input().split())

tools = list(map(int, input().split()))

tabs = [0 for _ in range(n)]
cnt = 0

for i, tool in enumerate(tools):
    if tool in tabs: continue
    elif 0 in tabs: tabs[tabs.index(0)] = tool
    else:
        last_used = 0
        swap_index = 0
        for j, used_tool in enumerate(tabs):
            if not used_tool in tools[i:]:
                swap_index = j
                break
            elif last_used < tools[i:].index(used_tool):
                last_used = tools[i:].index(used_tool)
                swap_index = j
            
        tabs[swap_index] = tool
        cnt += 1
        
print(cnt)