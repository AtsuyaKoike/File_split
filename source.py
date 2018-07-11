# coding: utf-8

import sys
import os
import random
import numpy as np
import shutil

print("loading...")

#----------------テストデータの割合設定------------------#
RAITO = 0.2
#--------------------------------------------------------#

'''
shutil.rmtree("//home//atsuya//data//validation//dogs//")
shutil.rmtree("//home//atsuya//data//validation//cats//")
shutil.rmtree("//home//atsuya//data//train//dogs//")
shutil.rmtree("//home//atsuya//data//train//cats//")
'''

#-------------------ディレクトリ作成----------------------#
os.makedirs("//home//atsuya//data//validation//dogs//")
os.makedirs("//home//atsuya//data//validation//cats//")
os.makedirs("//home//atsuya//data//train//dogs//")
os.makedirs("//home//atsuya//data//train//cats//")

#---------指定したディレクトリのファイル数を取得----------#
directory0 = os.listdir('//home//atsuya//dogs')
directory1 = os.listdir('//home//atsuya//cats')

size0 = len(directory0)
size1 = len(directory1)


#------------要素数分の配列を作成-------------#
#list0 = range( 1, size0 + 1 ) #python2.
#list1 = range( 1, size1 + 1 )
list0 = list(range(1, size0 + 1 ) ) #python3.
list1 = list(range(1, size1 + 1 ) )

#-----------配列の順番をシャッフル------------#
random.shuffle(list0)
random.shuffle(list1)

#---------------------ディレクトリ移動1----------------------#
directoryB = '//home//atsuya//data//validation//cats//'
directoryC = '//home//atsuya//data//train//cats//'
for i in range( size0 ):
	A = '//home//atsuya//cats//0//pic_'
	B = str( list0[i] )
	C = '.jpg'
	directory_all = A + B + C

	if ( i <= int( size0 * RAITO ) ):
		shutil.copy( directory_all, directoryB )
	else:
		shutil.copy( directory_all, directoryC )


#---------------------ディレクトリ移動2----------------------#
directoryB = '//home//atsuya//data//validation//dogs//'
directoryC = '//home//atsuya//data//train//dogs//'
for j in range( size1 ):
	A = '//home//atsuya//dogs//1//pic_'
	B = str( list1[j] )
	C = '.jpg'
	directory_all = A + B + C

	if ( j <= int( size1 * RAITO ) ):
		shutil.copy( directory_all, directoryB )
	else:
		shutil.copy( directory_all, directoryC )

#------------------終了-------------------#
print("finish!")


