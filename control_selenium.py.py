import pandas as pd 

from subprocess import Popen , PIPE
# import ast
# import tldextract
import time
def main(website,id):
    pass
    
        #    print(data)

if __name__ == '__main__':
    try:
        # MAKE A CSV FILE WHICH CONTAIN ID AND NO OF WEBSITE URL YOU WANT TO SCRAPY
        data = pd.read_excel('verfied_startup_new.xlsx')
        data_id       = data['id'].tolist()[:] 
        data_website = data['website'].tolist()[:]
        print(data_website)
        
        
        # THIS ITERATION LOOP WILL GET 40 URL AND NEXT 40 URL AND SO ON.
        j = 0
        for i in range(40,len(data_website),40):
            print(i)

            processes = []
            id,website = data_id[j:i],data_website[j:i]
            flags = 0
            # THIS ITERATION LOOP WILL SEND 40 URL AND CONCURRENTLY RUN THE MAIN FUNCTION USING SUBPROCESS
            for ids,href in zip(id,website):
                # if tldextract.extract(href).domain in scrape_website_domain_list:
                #     flags = 1
                print(ids,href)
                chrome_cmd = 'python3.7 products_script.py '+ str(href)+ ' ' + str(ids)
                processes.append(Popen(chrome_cmd, shell=True,stdin=None, stdout=None, stderr=None, close_fds=True))
                # break
                time.sleep(100)
                #stdout=PIPE, stderr=PIPE))
            # if flags == 1:
            #     flags = 0     
            for p in processes:
                data = p.communicate()
                print(data)
            # break
            j = i
            print(j)
    except:
        pass
