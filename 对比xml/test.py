import xml.etree.ElementTree as ET

import xml.etree.ElementTree as ET


def compare_hive_site_files(file1, file2):
    # 解析两个 XML 文件
    tree1 = ET.parse(file1)
    tree2 = ET.parse(file2)

    # 获取根节点
    root1 = tree1.getroot()
    root2 = tree2.getroot()

    # 遍历第一个文件中的节点
    for prop1 in root1.iter('property'):
        # 获取第一个文件中的 name 和 value 属性值
        name1 = prop1.find('name').text
        value1 = prop1.find('value').text

        # 在第二个文件中查找与该节点相对应的节点
        prop2 = root2.find('property[name="' + name1 + '"]')
        # 如果找到了相对应的节点
        if prop2 is not None:
            # 获取第二个文件中的 name 和 value 属性值
            name2 = prop2.find('name').text
            value2 = prop2.find('value').text

            # 比较两个节点的 value 属性值是否一致
            if value1 != value2:
                print("dev",name1,value1, "|\ttest:",value2)
        # 如果没找到相对应的节点
        else:
            print("dev",name1,"|\ttest:",value2)


compare_hive_site_files('hive-site-dev.xml', 'hive-site-test.xml')
