import argparse
import xml.etree.ElementTree as ET
import csv


def process_row(row_tag, weight_ref_dict):
    """
    <row>
        <sample-time id="1" fmt="00:29.312.581">29312581750</sample-time>
        <thread id="2" fmt="Main Thread  0xf588 (MemoryLeaks, pid: 366)">
            <tid id="3" fmt="0xf588">62856</tid>
            <process id="4" fmt="MemoryLeaks (366)">
                <pid id="5" fmt="366">366</pid>
                <device-session id="6" fmt="TODO">TODO</device-session>
            </process>
        </thread>
        <process ref="4"/>
        <core id="7" fmt="CPU 0">0</core>
        <thread-state id="8" fmt="Running">Running</thread-state>
        <weight id="9" fmt="1.00 ms">1000000</weight>
        <backtrace id="10" fmt="objc_msgSendSuper2 ← (16 other frames)">
            <process ref="4"/>
            <text-addresses id="11" fmt="frag 1383">7530229124 7532061922</text-addresses>
            <process ref="4"/>
            <text-addresses id="12" fmt="frag 688">7533405218 7532498034 7601621446 7601718626 7601734890 7601701222 7532718806 7532718638 7532716470 7532696038 7532694438 7701971778 7601095650 4306798446 7531153646</text-addresses>
        </backtrace>
    </row>
    :param tag:
    :Fetch value of self execution time and method
    :return:
    """
    fmt_weight = row_tag.findall('weight')[0].get('fmt', '')
    if fmt_weight:
            weight_ref_dict[row_tag.findall('weight')[0].get('id')] = fmt_weight
    else:
            fmt_weight = weight_ref_dict.get(row_tag.findall('weight')[0].get('ref'))
    fmt_backtrace = row_tag.findall('backtrace')[0].get('fmt', 'unknown')
    fmt_backtrace_b = fmt_backtrace.split('←')[0]
    return (fmt_weight, fmt_backtrace_b), weight_ref_dict


def sort(sub_li):
    """
    Sort rows on basis of sample time in descending order of self execution time
    """
    sub_li.sort(key=lambda x: x[0], reverse=True)
    return sub_li


def analyse(xmlFile: str, csvFile: str):
    """
    analyse a xml_file and store it to a csv file
    :param xml_file:
    :param save_path:
    :param process:
    :return:
    """
    tree = ET.parse(xmlFile)
    root = tree.getroot()
    row = []
    weight_ref_dict = {}
    for row_tag in root[0][1:]:
        data, weight_ref_dict = process_row(row_tag, weight_ref_dict)
        row.append(data)
    row_sorted = sort(row)
    with open(csvFile, "w", newline="") as f:
        writer = csv.writer(f)
        headers = ['Weight', 'Method name']
        writer.writerow(headers)
        writer.writerows(row_sorted)
        print(row_sorted)
        print('\n')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Trace Decoder')
    parser.add_argument('--xmlFile', type=str, default='recording',help='XML file')
    parser.add_argument('--csvFile', type=str, default=0,help='csv file')
    args = parser.parse_args()
    analyse(args.xmlFile, args.csvFile)
