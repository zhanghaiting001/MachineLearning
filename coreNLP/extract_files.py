import chardet

def Q2B_09az(char):
	if (char >= u'\uff10' and char <= u'\uff19') or (char >= u'\uff21' and char <= u'\uff3a') or (char >= u'\uff41' and char <= u'\uff5a'):
	    char = ord(char)
	    char -=0xfee0
	    char = chr(char)
	return char
def Q2B(uchar):
    """单个字符 全角转半角"""
    inside_code = ord(uchar) #具体哪些字符可以转，暂时不研究
    if inside_code == 0x3000:
        inside_code = 0x0020
    else:
        inside_code -= 0xfee0
    if inside_code < 0x0020 or inside_code > 0x7e: #转完之后不是半角字符返回原来的字符
        return uchar
    return chr(inside_code)

path = './news_tensite_xml.smarty.dat'
save_path = './news_smarty_title_content.txt'
#save_path_raw = './news_samrty_rawdata.txt'  #标题有的结尾为（,不过应该是原来数据就这样
file = open(path,'r',encoding='gb18030')
# decode('gbk','ignore') 不报错，但是有乱码
file_w = open(save_path,'w',encoding='utf-8') #默认就为utf-8
#file_wr = open(save_path_raw,'w',encoding='utf-8') #
for line in file.readlines():
	#可以有多种处理方法，一种是提取内容，一种是只提取汉字加数字字母常见标点（用jieba中re_han_default）
	if('<contenttitle>' in line):
		line = line.strip('</contenttitle>\n')+'\n'
	elif('<content>' in line):
		line = line.strip('</content>\n')+'\n'
	else:
		continue
	line_new =''
	for char in line:
		line_new += Q2B_09az(char)
	file_w.write(line_new)
	#file_wr.write(line)
file.close()
file_w.close()
#file_wr.close()

