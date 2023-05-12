import time
import asyncio
import threading
import multiprocessing
def bart(result):
    print('BART')
    time.sleep(5)
    result['BART']='b'
    print('BART DONE')
def peg(result):
    print('PEG')
    time.sleep(1)
    result['PEG']='p'
    print('PEG DONE')
def main():
    result = {}
    result['A']='a'
    functios = [bart,peg]
    threads = []
    for func in functios:
        t=threading.Thread(target=func,args=[result])
        t.start()
        threads.append(t)
    for thread in threads:
        thread.join()
    print(result)
main()
"""
t1 = threading.Thread(target=bart,args=['bart'])
    t2 = threading.Thread(target=peg,args=['peg'])
    t1.start()
    t2.start()
"""