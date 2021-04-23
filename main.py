from PIL import Image

# don't change
input_operation_list = 'operators.txt'


# rename 'skill_example.txt' as 'skill.txt'
input_skill_list = 'skills.txt'


# if no left [ID Card] then set to 0
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
display_class_icon = False


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


def print_operator(op, sk):

    # check qualifications
    if (sk['skill1'] + sk['skill2'] + sk['skill3'] <= 0 and master_only):
        return

    # debug
    # print(op['name'])
    print('正在打印：' + sk['name'] + '\n')

    # cnt
    mcnt[sk['skill1']] += 1
    mcnt[sk['skill2']] += 1
    mcnt[sk['skill3']] += 1

    # change position
    global startX, line, startY, bg
    if (startX + slot_width > bg.width - right_indent):
        line += 1
        startX = line * line_diff + left_indent
        startY += slot_height

    # load images
    img1 = Image.open('resource/Slot - single - background.png')
    img2 = Image.open('avatar/' + op['filename'] + '_' + str(sk['costume']) + '.png')
    img3 = Image.open('resource/Slot - single  精二+黑遮罩.png')
    img4 = Image.open('resource/Akteam-rarity_' + op['rare'] + '.png')
    img5 = Image.open('resource/潜能' + str(sk['potential']) + '.png')
    img6 = Image.open('resource/' + str((sk['level'] // 10) * 10) + '.png')
    img7 = Image.open('resource/专精' + str(sk['skill1']) + '.png')
    img8 = Image.open('resource/专精' + str(sk['skill2']) + '.png')
    img9 = Image.open('resource/专精' + str(sk['skill3']) + '.png')

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
    if (op['rare'] == '6' or op['name'] == '阿米娅'):
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


if __name__ == "__main__":

    with open(input_operation_list, 'r', encoding='utf-8') as f:
        operator = eval('[' + f.read() + ']')

    with open(input_skill_list, 'r', encoding='utf-8') as f:
        skill = eval('[' + f.read() + ']')

    num = 8
    for sk in skill:

        # 顺便的
        if (sk['skill1'] + sk['skill2'] + sk['skill3'] > 0 or not master_only):
            num += 1

        posclass = ''
        for op in operator:
            if (sk['name'] == op['name']):
                posclass = op['class']

        sk['class'] = posclass

    if (display_class_icon):
        skill = sorted(skill, key=lambda i: (
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

    for sk in skill:

        pos = ''
        for op in operator:
            if (op['name'] == sk['name']):
                pos = op
                # print("matched! :" + op['name']+ '\n')

        if (current_class != pos['class']):
            current_class = pos['class']
            if (display_class_icon):
                print_class(current_class)
        print_operator(pos, sk)

    print('\n干员数量统计 ' + str(num))
    print('\n专精数量统计[专0，专1，专2，专3] = ' + str(mcnt))

    if (scale != 1.0):
        bg_ratio = bg.height / bg.width
        bg = bg.resize(
            (int(bg.width * scale), int(bg.width * scale * bg_ratio)), Image.ANTIALIAS)

    bg.show()

    zs, xs = str(scale * 100).split('.')
    bg.convert('RGB').convert('RGBA').save('result-c-' + str(zs) + '%.png')
