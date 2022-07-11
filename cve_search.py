def cve_search(app,version,scan_time):
    print(f"[INFO] cve search app: {app}:{version}")
    scan_time = 0
    print(app,version,scan_time)
    full_app=str(app)

    if version != '':
        full_app=full_app+':'+str(version)
    result_url='/result/'+full_app
    cve_search = ['/cve-search/bin/search.py', '-p', full_app,'-o','csv']
    null='unknown'
    if path.exists(result_url+'.csv'):
        return "exist"
        #xu ly
        if (time() - path.getmtime(result_url+'.csv'))> int(scan_time):
            result = cmd_runner(cve_search)
            #,'>>',result_url+'.csv'
            fr=open(result_url+'.csv','w')
            fr.write(result)
            fr.close()
            return "Success"
        return "exist"
    else:
        result = cmd_runner(cve_search)
        fr=open(result_url+'.csv','w')
        fr.write(result)
        fr.close()
        return "Success"
