from topoly.topoly_homfly import find_link_code_to_string
data_dir = 'data'
print(find_link_code_to_string([(data_dir + '/arc1').encode('utf-8'), (data_dir + '/arc2').encode('utf-8'), (data_dir + '/arc3').encode('utf-8')], yamada=True))