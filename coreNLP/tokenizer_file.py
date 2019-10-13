import argparse
import os
import logging
import sys
import jieba
from stanfordcorenlp import StanfordCoreNLP

logger = logging.getLogger()
console = logging.StreamHandler()
logger.setLevel(logging.WARNING)  #正式改为DEBUG INFO WARNING ERROR CRITICAL
#这个能控制stanford
logger.addHandler(console)


def jieba_tokenizer(file_names,save_path):
    for file in file_names:
        save_name = save_path +'jieba_'+os.path.basename(file)
        f = open(file,'r',encoding='utf-8')
        f_w = open(save_name,'w',encoding='utf-8')
        for line in f.readlines():
            seg_gen = jieba.cut(line, cut_all=False)
            f_w.write(' '.join(seg_gen))
        f.close()
        f_w.close()


def stanford_tokenizer(file_names,save_path):
    nlp = StanfordCoreNLP(r'/home/zht/pythoncode/pytorch/DrQA/data/corenlp/',lang='zh')
    for file in file_names:
        save_name = save_path +'stanford_'+os.path.basename(file)
        f = open(file,'r',encoding='utf-8')
        f_w = open(save_name,'w',encoding='utf-8')
        for line in f.readlines():
            if line!='\n':
                seg_list = nlp.word_tokenize(line) #line是空格时报错
                f_w.write(' '.join(seg_list)+'\n')
        f.close()
        f_w.close()


def tokenizer_file(input_path,save_path=None,tokenizer='jieba'):

    if tokenizer == 'jieba': 
        use_jieba = True
        use_stanford = False
    elif tokenizer == 'stanford':
        use_jieba = False
        use_stanford = True
    elif tokenizer == 'all':
         use_jieba = True
         use_stanford = True
    else:
        use_jieba = True          #输入任何错误的字符，也用jieba
        use_stanford = False

    
    file_names =[]
    if os.path.isfile(input_path):
        file_names.append(input_path)
    elif os.path.isdir(input_path):
        for name in os.listdir(input_path):
            #file_names.append(args.input_path.strip('/')+'/'+name)  #针对文件路径为./.. 未加/的
            file_names.append(input_path+name)
    else:
        raise RuntimeError('Invalid input_path name!') #异常，退出程序
    logger.debug(file_names)

    if save_path == None or os.path.isdir(save_path)== False:
        abs_path = os.path.abspath(input_path)
        save_path = os.path.dirname(abs_path)+'/'  #如果input_path是folder必须以/结尾,否则dirname会得到再上一层

    if use_jieba:
        jieba_tokenizer(file_names,save_path)
    if use_stanford:
        stanford_tokenizer(file_names,save_path)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_path',type=str,help='the file or folder,folder is end by /')
    parser.add_argument('--save_path',type=str,default=None,help='folder,default is the same folder with input')
    parser.add_argument('--tokenizer',type=str,default='jieba',help='jieba,standford,or all, for compare')
    args = parser.parse_args()
    logger.debug(args)  #Namespace(input_path=None, save_path=None, tokenizer='all')
     
    tokenizer_file(args.input_path,args.save_path,args.tokenizer)