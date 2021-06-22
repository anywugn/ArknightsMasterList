from PIL import Image, ImageFont, ImageDraw
from openpyxl import load_workbook
import sys


# don't change
input_operation_list = 'operators.txt'


# rename 'skill_example.txt' as 'skill.txt'
input_skill_list = 'skills.txt'


# with [ID Card] then set to about 407
left_indent = 407


# right bound
right_indent = 0

# upper bound
startY = 28

# make each line start at different point
line_diff = 70

# relative path of background image, use gray if leave empty
background_png = ''

# size of image if no background image specified
usr_bg_width = 5000
usr_bg_height = 1080

# only display operators with master skills
master_only = True

# class icon is cooooool but you can turn it off anyway
display_class_icon = True

# sort by class, then level
list_sorted = False

# the final scale of output image, 1.0 = 100% = No Scale
scale = 1.0


# don't change
line = 0
cnt = 0
slot_width = 0
slot_height = 0
bg_width = 0
bg_height = 0
startX = left_indent
bg = ''
current_class = ''
mcnt = [0, 0, 0, 0]
furniture_cnt = 766
furniture_total = 776
medal_cnt = 213
medal_total = 213
operator_cnt = 188
operator_total = 188
doctor_level = 120
doctor_name = '凯尔希'
doctor_no = 3989


def print_operator(op):

    # check qualifications
    if (op['skill1'] + op['skill2'] + op['skill3'] <= 0 and master_only):
        return

    # debug
    # print(op['name'])
    print('正在打印：' + op['name'] + '\n')

    # cnt
    mcnt[op['skill1']] += 1
    mcnt[op['skill2']] += 1
    mcnt[op['skill3']] += 1



    # change position
    global startX, line, startY, bg
    if (startX + slot_width > bg.width - right_indent):
        line += 1
        startX = line * line_diff + left_indent
        startY += slot_height

    # load images
    img1 = Image.open('resource/Slot - single - background.png')
    img2 = Image.open('avatar/' + op['filename'] + '_' + str(op['costume']) + '.png')
    img3 = Image.open('resource/Slot - single  精二+黑遮罩.png')
    img4 = Image.open('resource/Akteam-rarity_' + str(op['rare']) + '.png')
    img5 = Image.open('resource/潜能' + str(op['potential']) + '.png')
    img6 = Image.open('resource/' + str((op['level'] // 10) * 10) + '.png')
    img7 = Image.open('resource/专精' + str(op['skill1']) + '.png')
    img8 = Image.open('resource/专精' + str(op['skill2']) + '.png')
    img9 = Image.open('resource/专精' + str(op['skill3']) + '.png')

    # adjust images

    # print(str(img2.width) + '  ' + str(img2.height))
    ratio = img2.height / img2.width
    img2 = img2.resize((135, int(135 * ratio)), Image.ANTIALIAS)

    # paste images
    bg.paste(img1, (startX, startY), mask=img1.split()[3])
    bg.paste(img2, (startX + 12, startY + 284 - img2.height), mask=img2)
    bg.paste(img3, (startX + 12, startY + 284 - img3.height), mask=img3)
    bg.paste(img4, (startX + 12, startY + 284 - img4.height), mask=img4)
    bg.paste(img5, (startX + 22, startY + 244), mask=img5)
    bg.paste(img6, (startX + 108, startY + 250), mask=img6)
    bg.paste(img7, (startX + 17, startY + 292), mask=img7)
    bg.paste(img8, (startX + 62, startY + 292), mask=img8)
    if (op['rare'] == 6 or op['name'] == '阿米娅'):
        bg.paste(img9, (startX + 107, startY + 292), mask=img9)

    startX += slot_width
    # print('\n')


def print_class(class_name):
    global startX, line, startY, bg
    if (startX + slot_width > bg.width - right_indent):
        line += 1
        startX = line * line_diff + left_indent
        startY += slot_height

    img1 = Image.open('resource/职业_' + class_name + '.png')
    bg.paste(img1, (startX, startY), mask=img1.split()[3])

    startX += slot_width


def get_font_render_width(text, fontsize):
    canvas = Image.new('RGB', (2048, 2048))
    draw = ImageDraw.Draw(canvas)
    path_to_ttf = r'c:\windows\fonts\msyh.ttc'
    monospace = ImageFont.truetype(path_to_ttf, fontsize)
    draw.text((0, 0), text, font=monospace, fill=(5, 5, 5))
    bbox = canvas.getbbox()
    width = bbox[2] - bbox[0]
    return width


if __name__ == "__main__":

    wb = load_workbook(filename='aml-input.xlsx')
    ss = wb['skills']  # skill sheet


    ss_dict = []

    for row_objects in ss:
        if row_objects[0].row != 1 and row_objects[1].value is not None:
            ss_dict.append({'name': row_objects[0].value,
                            'costume': row_objects[1].value,
                            'potential': row_objects[2].value,
                            'level': row_objects[3].value,
                            'skill1': row_objects[4].value,
                            'skill2': row_objects[5].value,
                            'skill3': row_objects[6].value,
                            'filename': row_objects[7].value,
                            'rare': row_objects[8].value,
                            'class': row_objects[9].value
                            })
            for k in ss_dict[-1]:
                if ss_dict[-1][k] is None:
                    ss_dict[-1][k] = 0






    num = 0
    for sk in ss_dict:

        # 顺便的
        if (sk['skill1'] + sk['skill2'] + sk['skill3'] > 0 or not master_only):
            num += 1

    if (list_sorted or display_class_icon):
        ss_dict = sorted(ss_dict, key=lambda i: (
            i['class'], i['level']), reverse=True)

    print('您一共有 ' + str(num) + ' 个干员要打印\n')





    if (background_png != ''):
        bg = Image.open(background_png)
    else:
        bg = Image.new('RGBA', (usr_bg_width, usr_bg_height),
                       (49, 49, 49, 255))

    bg_height = bg.height
    bg_width = bg.width

    img0 = Image.open('resource/Slot - single - background.png')
    slot_width = img0.width
    slot_height = img0.height

    for op in ss_dict:

        if current_class != op['class']:
            current_class = op['class']
            if display_class_icon:
                print_class(current_class)
        print_operator(op)





    print('\n干员数量统计 ' + str(num))
    print('\n专精数量统计[专0，专1，专2，专3] = ' + str(mcnt))

    # adding namecard
    namecard_img = Image.open('resource/namecard-v2-empty.png')
    bg.paste(namecard_img, (0, 0), mask=namecard_img)



    path_to_ttf = r'c:\windows\fonts\msyh.ttc'
    # 入职日期
    draw = ImageDraw.Draw(bg)
    font = ImageFont.truetype(path_to_ttf, size=25)
    draw.text(xy=(123, 28), text='2019-04-30', font=font, fill=(0, 0, 0,255))
    draw.text(xy=(123, 77), text='2021-06-22', font=font, fill=(0, 0, 0,255))

    # 专精数量
    font = ImageFont.truetype(path_to_ttf, size=34)
    # 专3
    tri_mid = 68
    draw.text(xy=(tri_mid - (18 * len(str(mcnt[3])) / 2) - 3 + 1, 233 + 1), text=str(mcnt[3]), font=font, fill=(0, 0, 0, 255))
    draw.text(xy=(tri_mid - (18 * len(str(mcnt[3])) / 2) - 3, 233), text=str(mcnt[3]), font=font, fill=(255, 255, 255, 255))
    # 专2
    tri_mid = 164
    draw.text(xy=(tri_mid - (18 * len(str(mcnt[2])) / 2) - 3 + 1, 233 + 1), text=str(mcnt[2]), font=font, fill=(0, 0, 0, 255))
    draw.text(xy=(tri_mid - (18 * len(str(mcnt[2])) / 2) - 3, 233), text=str(mcnt[2]), font=font, fill=(255, 255, 255, 255))
    # 专1
    tri_mid = 259
    draw.text(xy=(tri_mid - (18 * len(str(mcnt[1])) / 2) - 3 + 1, 233 + 1), text=str(mcnt[1]), font=font, fill=(0, 0, 0, 255))
    draw.text(xy=(tri_mid - (18 * len(str(mcnt[1])) / 2) - 3, 233), text=str(mcnt[1]), font=font, fill=(255, 255, 255, 255))

    # 家具
    font = ImageFont.truetype(path_to_ttf, size=22)
    draw.text(xy=(30, 350), text=str(furniture_cnt), font=font, fill=(251, 225, 111, 255))
    draw.text(xy=(30 + 13 * len(str(furniture_cnt)) - 1, 350), text='/' + str(furniture_total), font=font, fill=(255, 255, 255, 255))

    # 蚀刻章
    font = ImageFont.truetype(path_to_ttf, size=22)
    draw.text(xy=(180, 350), text=str(medal_cnt), font=font, fill=(251, 225, 111, 255))
    draw.text(xy=(180 + 13 * len(str(medal_cnt)) - 1, 350), text='/' + str(medal_total), font=font, fill=(255, 255, 255, 255))

    # 雇佣干员数
    font = ImageFont.truetype(path_to_ttf, size=65)
    draw.text(xy=(29, 445), text=str(operator_cnt), font=font, fill=(251, 225, 111, 255))
    draw.text(xy=(29 + 38 * len(str(operator_cnt)) - 1, 445), text='/' + str(operator_total), font=font, fill=(255, 255, 255, 255))



    # 头像
    # (107,721)
    # 232 * 232


    # 博士等级
    doctor_level_img = Image.open('resource/doctor-level-mask.png')
    bg.paste(doctor_level_img, (63, 676), mask=doctor_level_img)
    font = ImageFont.truetype(path_to_ttf, size=47)
    mid = 110
    draw.text(xy=(110 - (27 * len(str(doctor_level))) / 2, 695), text=str(doctor_level), font=font, fill=(255, 255, 255, 255))


    # 博士名字
    dr_doctor_name = 'Dr.' + doctor_name + '#' + str(doctor_no)
    doctor_name_fontsize = 63
    while get_font_render_width(dr_doctor_name, doctor_name_fontsize) > 520:
        doctor_name_fontsize -= 5

    font = ImageFont.truetype(path_to_ttf, size=doctor_name_fontsize)
    draw.text(xy=(10, 967), text=str('Dr.' + doctor_name), font=font, fill=(255, 255, 255, 255))
    draw.text(xy=(10 + get_font_render_width('Dr.' + doctor_name, doctor_name_fontsize) + 10, 967), \
        text=str( '#' + str(doctor_no)), font=font, fill=(243, 164, 57, 255))



    # scale begins, no changes to image beyond this point
    if (scale != 1.0):
        bg_ratio = bg.height / bg.width
        bg = bg.resize(
            (int(bg.width * scale), int(bg.width * scale * bg_ratio)), Image.ANTIALIAS)

    bg.show()

    zs, xs = str(scale * 100).split('.')
    bg.convert('RGB').convert('RGBA').save('result-c-' + str(zs) + '%.png')
