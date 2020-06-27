def killProcess(pid, ppid, kill):
    ppid_set = set(ppid)
    def kill_by_dfs(pid, ppid, kill):
        if not kill in ppid_set:
            return [kill]
        res = []
        for pp in [pid[i] for i, _ in enumerate(ppid) if ppid[i] == kill]:
            res.extend(kill_by_dfs(pid, ppid, pp))
        res.append(kill)
        return res
    return kill_by_dfs(pid, ppid, kill)