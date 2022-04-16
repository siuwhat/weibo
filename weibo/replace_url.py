def get_replaced_url(url:str,max_id):
    url_list=url.split("&")
    for i in range(len(url_list)):
        if "max_id" in url_list[i]:
            url_list[i]=url_list[i][:7]+str(max_id)
    newurl="&".join(url_list)
    return newurl
