'''matplotlib(三)——Working with text    https://blog.csdn.net/qq_31192383/article/details/54380736''''''下面这些命令是在pyplot用户界面中创建文本：text()——在axes中任意位置添加文本xlabel()——在X轴上添加轴标签ylabel()——在Y轴上添加轴标签title()——给axes添加标题figtext()——给一个figure中任意位置添加文本suptitle()——给一个figure添加标题annotate()——在axes中添加批注，可带有箭'''# -*- coding: utf-8 -*-import matplotlib.pyplot as pltimport matplotlib.patches as patchesdef hello_world():    fig = plt.figure()    fig.suptitle('use suptitle()', fontsize=14, fontweight='bold')    ax = fig.add_subplot(111)    fig.subplots_adjust(top=0.85)    ax.set_title('use set_title()')    ax.set_xlabel('use set_xlabel')    ax.set_ylabel('use set_ylabel')    ax.text(3, 8, 'use text() in data coords', style='italic', bbox={'facecolor': 'red', 'alpha': 0.5, 'pad': 10})    ax.text(2, 6, r'an equation: $E=mc^2$', fontsize=15)    ax.text(3, 2, u'unicode: Institut f\374r Festk\366rperphysik')    # 你可以使用horizontalalignment, verticalalignment, 或者multialignment属性来设置文本的对其方式。    # horizontalalignment控制X方向上文本位于左右还是居中显示，verticalalignment则是控制文本的上下还是居中显示。    ax.text(0.95, 0.01, 'colored text in axes coords', verticalalignment='bottom', horizontalalignment='right',            transform=ax.transAxes, color='green', fontsize=15)    ax.plot([2], [1], 'o')    ax.annotate('use annotate()', xy=(2, 1), xytext=(3, 4),                arrowprops=dict(facecolor='black', shrink=0.05))    ax.axis([0, 10, 0, 10])    plt.show()    plt.close()    pass'''你可以使用horizontalalignment, verticalalignment, 或者multialignment属性来设置文本的对齐方式。horizontalalignment控制X方向上文本位于左右还是居中显示，verticalalignment则是控制文本的上下还是居中显示。 '''def text_location():    # build a rectangle in axes coords    left, width = .25, .5    bottom, height = .25, .5    right = left + width    top = bottom + height    fig = plt.figure()    ax = fig.add_subplot(111)    # axes coordinates are 0,0 is bottom left and 1,1 is upper right    # transform = ax.transAxes: 说明坐标轴是以axes坐标系为标准的，(0, 0)就是axes的左下角，(1, 1)是右上角。    p = patches.Rectangle((left, bottom), width, height, fill=False, transform=ax.transAxes, clip_on=False)    ax.add_patch(p)    ax.text(left, top, 'left top', horizontalalignment='left', verticalalignment='top', transform=ax.transAxes)    ax.text(left, bottom, 'left bottom', horizontalalignment='left', verticalalignment='bottom', transform=ax.transAxes)    ax.text(right, bottom, 'right bottom', horizontalalignment='right', verticalalignment='bottom', transform=ax.transAxes)    ax.text(right, top, 'right top', horizontalalignment='right', verticalalignment='top', transform=ax.transAxes)    ax.text(right, bottom, 'center top', horizontalalignment='center', verticalalignment='top', transform=ax.transAxes)    ax.text(left, 0.5 * (bottom + top), 'right center', horizontalalignment='right', verticalalignment='center',            rotation='vertical', transform=ax.transAxes)    ax.text(left, 0.5 * (bottom + top), 'left center', horizontalalignment='left', verticalalignment='center',            rotation='vertical', transform=ax.transAxes)    ax.text(0.5 * (left + right), 0.5 * (bottom + top), 'middle', horizontalalignment='center',            verticalalignment='center', fontsize=20, color='red', transform=ax.transAxes)    ax.text(right, 0.5 * (bottom + top), 'centered', horizontalalignment='center', verticalalignment='center',            rotation='vertical', transform=ax.transAxes)    ax.text(left, top, 'rotated\nwith newlines', horizontalalignment='center', verticalalignment='center',            rotation=45, transform=ax.transAxes)    # ax.set_axis_off()    plt.show()    plt.close()    passif __name__ == '__main__':    text_location()    pass