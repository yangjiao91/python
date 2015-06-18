#-*- coding: utf-8 -*-

lost_key = []
excess_key = []
dict_res = {}
err_value_res = []
dict_res_string = ''
actual_value_res = {}
expected_value_res = {}
err_value_res_item = {}
incorrect_number = {}
correct_number = {}
last_element = ''
def compareDict(contrast_dict,standard_dict,root_node,completeurl,is_new):
        global temp_node
        global lost_key
        global excess_key
        global err_value_res
        global dict_res
        global dict_res_string

        if is_new=='new':
            lost_key = []
            excess_key = []
            dict_res = {}
            dict_res_string = ''
            actual_value_res = {}
            expected_value_res = {}
            err_value_res_item = {}
            err_value_res = []
            incorrect_number = {}
            correct_number = {}
            print 'newnewnwe:',dict_res_string
        print 'oldoldold:',dict_res_string

        temp_node = root_node
        print '4444temp_node4444: ',temp_node

        import simplejson
        try:
            contrast_dict = simplejson.loads(contrast_dict)
        except Exception,ex:
            return "actual result return Error message, Json resolution fail"
        try:
            standard_dict = simplejson.loads(standard_dict)
        except Exception,ex:
            return "expected result Json resolution fail"

        print 'contrast_dict ',contrast_dict
        print 'standard_dict ',standard_dict        
       
        # 返回结果缺少字段
        #print '--standard_dict.keys()',standard_dict.keys()
        #print '--contrast_dict.keys()',contrast_dict.keys()
        for key in standard_dict.keys():
            if contrast_dict.keys().count(key) == 0:
                print 'lost key: ',key
                lost_key_item = temp_node + key + '/'
                lost_key.append(lost_key_item)
                dict_res['lost_key'] = lost_key
                dict_res['url'] = completeurl
                dict_res_string = simplejson.dumps(dict_res)
                
        # 返回结果多了字段
        for key in contrast_dict.keys():
            print '777temp_node: ',temp_node
            if standard_dict.keys().count(key) == 0: 
                excess_key_item = temp_node + key + '/'
                excess_key.append(excess_key_item)
                dict_res['excess_key'] = excess_key
                dict_res['url'] = completeurl
                dict_res_string = simplejson.dumps(dict_res)
            
            # 如果字段的值是字典，递归  
            elif isinstance(contrast_dict[key],dict):
                print '55555temp_node: ',temp_node
                print 'simplejson.dumps(contrast_dict[key]): ',simplejson.dumps(contrast_dict[key]),'  endsimplejson.dumps(contrast_dict[key])','***key*:',key
                if isinstance(standard_dict[key],dict):
                    temp_node_list=temp_node.split('/')
                    if len(temp_node_list)-2>0:
                        temp =temp_node_list[len(temp_node_list)-2].split('[')[0]
                        if contrast_dict.keys().count(temp)>0:
                            del temp_node_list[len(temp_node_list)-2]
                            s='/'
                            temp_node = s.join(temp_node_list)
                    if len(temp_node_list)-3>0:
                        temp =temp_node_list[len(temp_node_list)-3].split('[')[0]
                        if contrast_dict.keys().count(temp)>0:
                            del temp_node_list[len(temp_node_list)-3]
                            s='/'
                            temp_node = s.join(temp_node_list)
                    temp_node = temp_node + key + '/'
                    dict_res_string=compareDict(simplejson.dumps(contrast_dict[key]),simplejson.dumps(standard_dict[key]),temp_node,completeurl,'old')
                else:
                    actual_value_res={}
                    expected_value_res={}
                    actual_value_res[temp_node+key+'/'] = "the type is {}"
                    expected_value_res[temp_node+key+'/'] = "the type is not {}"
                    err_value_res_item={}
                    err_value_res_item['actual_result'] = actual_value_res
                    err_value_res_item['expected_result'] = expected_value_res
                    err_value_res.append(err_value_res_item)
                    dict_res['eliments_type_is_incorrect'] = err_value_res
                    dict_res['url'] = completeurl
                    dict_res_string = simplejson.dumps(dict_res)


            # 如果字段的是数组，遍历每一个元素
            elif isinstance(contrast_dict[key],list):
                # 如果数组里的元素个数不相同，报错
                if(len(contrast_dict[key])!=len(standard_dict[key])):
                    incorrect_number = {}
                    correct_number = {}
                    incorrect_number[temp_node+key+'/'] =  len(contrast_dict[key])
                    correct_number[temp_node+key+'/'] =  len(standard_dict[key])
                    err_value_res_item={}
                    err_value_res_item['actual_result'] = incorrect_number
                    err_value_res_item['expected_result'] = correct_number
                    err_value_res.append(err_value_res_item)
                    dict_res['the_number_of_eliments_in_the_array_is_incorrect'] = err_value_res
                    dict_res['url'] = completeurl
                    dict_res_string = simplejson.dumps(dict_res)
                else:
                    for i in range(len(contrast_dict[key])):
                        if i>0:
                            last_elememt = ''
                            last_elememt = key + '[' + str(i-1) + ']'
                            print 'last_elememt',last_elememt
                            print 'temp_node.split(last_elememt)',temp_node.split(last_elememt)
                            if temp_node.find(last_elememt)>0:    
                                temp_node = (temp_node.split(last_elememt))[0] 
                        # 如果数组的元素是字典，递归,否则直接比较元素
                        if isinstance(contrast_dict[key][i],dict):
                            if isinstance(standard_dict[key][i],dict):
                                temp_node_list=temp_node.split('/')
                                if len(temp_node_list)-2>0:
                                    temp =temp_node_list[len(temp_node_list)-2].split('[')[0]
                                    if contrast_dict.keys().count(temp)>0:
                                        del temp_node_list[len(temp_node_list)-2]
                                        s='/'
                                        temp_node = s.join(temp_node_list)
                                temp_node = temp_node + key + '[' + str(i) + ']' + '/'
                                dict_res_string= compareDict(simplejson.dumps(contrast_dict[key][i]),simplejson.dumps(standard_dict[key][i]),temp_node,completeurl,'old')
                            else :
                                actual_value_res={}
                                expected_value_res={}
                                actual_value_res[temp_node+key+'/'] = "the type is {}"
                                expected_value_res[temp_node+key+'/'] = "the type is not {}"
                                err_value_res_item={}
                                err_value_res_item['actual_result'] = actual_value_res
                                err_value_res_item['expected_result'] = expected_value_res
                                err_value_res.append(err_value_res_item)
                                dict_res['eliments_type_is_incorrect'] = err_value_res
                                dict_res['url'] = completeurl
                                dict_res_string = simplejson.dumps(dict_res)
                        else:
                            if contrast_dict[key][i] != standard_dict[key][i]:
                                 err_value_res_key = temp_node + key + '/'
                                 actual_value_res={}
                                 expected_value_res={}
                                 actual_value_res[err_value_res_key] = contrast_dict[key]
                                 expected_value_res[err_value_res_key] = standard_dict[key]
                                 err_value_res_item={}
                                 err_value_res_item['actual_result'] = actual_value_res
                                 err_value_res_item['expected_result'] = expected_value_res
                                 err_value_res.append(err_value_res_item)
                                 dict_res['same_key_but_different_values'] = err_value_res
                                 dict_res['url'] = completeurl
                                 dict_res_string = simplejson.dumps(dict_res)                                 
             
            else: 
                import sys
                reload(sys)
                sys.setdefaultencoding('utf-8')
                print ' !!! ' + key  
                print 'contrast_dict[key] ' ,contrast_dict[key] 
                print 'tandard_dict[key] ' ,standard_dict[key]
                if contrast_dict[key] != standard_dict[key]:
                    err_value_res_key = temp_node + key + '/'
                    actual_value_res={}
                    expected_value_res={}
                    actual_value_res[err_value_res_key] = contrast_dict[key]
                    expected_value_res[err_value_res_key] = standard_dict[key]
                    err_value_res_item={}
                    err_value_res_item['actual_result'] = actual_value_res
                    err_value_res_item['expected_result'] = expected_value_res
                    err_value_res.append(err_value_res_item)

                    dict_res['same_key_but_different_values'] = err_value_res
                    dict_res['url'] = completeurl
                    dict_res_string = simplejson.dumps(dict_res)
        return dict_res_string

        
a='{"return":"succ","data":[{"type":"mobile_notice","mid":"","picurl":"http:\/\/img.funshion.com\/attachment\/new_images\/2013\/12-25\/42024649_1387964530_845.jpg","durl":"http:\/\/adk.funshion.com\/adpolestar\/wayl\/;ad=8D75484B_D87F_690C_BDAC_78F8EDDFC51D;ap=0;pu=funshion;\/?http:\/\/www.hui3g.com\/jump\/427&fscli=iphone&fsver=1.2.9.2","program_type":"0","purl":"","mpurl":"","mpurls":{}},{"type":"mobile_notice","mid":"","picurl":"http:\/\/img.funshion.com\/attachment\/new_images\/2014\/01-02\/42024649_1388628848_431.jpg","durl":"http:\/\/um0.cn\/IENRf?fscli=iphone&fsver=1.2.9.2","program_type":"0","purl":"","mpurl":"","mpurls":{}},{"type":"mobile_media","mid":"99934","picurl":"http:\/\/img.funshion.com\/attachment\/new_images\/2012\/11-19\/18395589_1353322194_391.jpg","durl":"","program_type":"0","purl":"","mpurl":"","mpurls":{}},{"type":"mobile_media","mid":"94945","picurl":"http:\/\/img.funshion.com\/attachment\/new_images\/2012\/11-21\/18395589_1353490373_793.jpg","durl":"","program_type":"0","purl":"","mpurl":"","mpurls":{}},{"type":"mobile_media","mid":"97742","picurl":"http:\/\/img.funshion.com\/attachment\/new_images\/2012\/11-19\/18395589_1353321548_833.jpg","durl":"","program_type":"0","purl":"","mpurl":"","mpurls":{}},{"type":"mobile_media","mid":"98482","picurl":"http:\/\/img.funshion.com\/attachment\/new_images\/2012\/11-19\/18395589_1353320936_309.jpg","durl":"","program_type":"0","purl":"","mpurl":"","mpurls":{}}]}'

b='{"data":[{"type":"mobile_test","mid":"","picurl":"http:\/\/img.funshion.com\/attachment\/new_images\/2013\/12-25\/42024649_1387964530_845.jpg","durl":"http:\/\/adk.funshion.com\/adpolestar\/wayl\/;ad=8D75484B_D87F_690C_BDAC_78F8EDDFC51D;ap=0;pu=funshion;\/?http:\/\/www.hui3g.com\/jump\/427&fscli=iphone&fsver=1.2.9.2","program_type":"0","purl":"","mpurl":"","mpurls":{}},{"type":"mobile_notice","mid":"","picurl":"http:\/\/img.funshion.com\/attachment\/new_images\/2014\/01-02\/42024649_1388628848_431.jpg","durl":"http:\/\/um0.cn\/IENRf?fscli=iphone&fsver=1.2.9.2","program_type":"0","purl":"","mpurl":"","mpurls":{}},{"type":"mobile_media","mid":"99934","picurl":"http:\/\/img.funshion.com\/attachment\/new_images\/2012\/11-19\/18395589_1353322194_391.jpg","durl":"","program_type":"0","purl":"","mpurl":"","mpurls":{}},{"type":"mobile_media","mid":"94945","picurl":"http:\/\/img.funshion.com\/attachment\/new_images\/2012\/11-21\/18395589_1353490373_793.jpg","durl":"","program_type":"0","purl":"","mpurl":"","mpurls":{}},{"type":"mobile_media","mid":"97742","picurl":"http:\/\/img.funshion.com\/attachment\/new_images\/2012\/11-19\/18395589_1353321548_833.jpg","durl":"","program_type":"0","purl":"","mpurl":"","mpurls":{}},{"type":"mobile_media","mid":"98482","picurl":"http:\/\/img.funshion.com\/attachment\/new_images\/2012\/11-19\/18395589_1353320936_309.jpg","durl":"","program_type":"0","purl":"","mpurl":"","mpurls":{}}]}'





#compareDict(c,d)
