# @Time : 2024/5/30 0:36
# 论文作图代码
import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    # import matplotlib.pyplot as plt
    #
    # # 指标类型和数据
    # models = ['SRCNN', 'RCAN']
    # set5 = [5.78, 2.84]
    # set14 = [4.11, 2.18]
    # BSD100 = [2.60, 1.14]
    # Urban100 = [8.80, 3.93]
    #
    # # 创建柱状图
    # fig, ax = plt.subplots()
    # bar_width = 0.2
    # index = range(len(models))
    #
    # bar1 = ax.bar(index, set5, bar_width, label='Set5')
    # bar2 = ax.bar([i + bar_width for i in index], set14, bar_width, label='Set14')
    # bar3 = ax.bar([i + 2 * bar_width for i in index], BSD100, bar_width, label='BSD100')
    # bar4 = ax.bar([i + 3 * bar_width for i in index], Urban100, bar_width, label='Urban100')
    #
    #
    # # 添加数据标签
    # def add_labels(bars):
    #     for bar in bars:
    #         height = bar.get_height()
    #         ax.annotate(f'{height:.2f}%',
    #                     xy=(bar.get_x() + bar.get_width() / 2, height),
    #                     xytext=(0, 3),
    #                     textcoords="offset points",
    #                     ha='center', va='bottom')
    #
    #
    # add_labels(bar1)
    # add_labels(bar2)
    # add_labels(bar3)
    # add_labels(bar4)
    #
    # # 添加标签
    # ax.set_xlabel('Models')
    # ax.set_ylabel('Performance Improvement (%)')
    # ax.set_title('PSNR')
    # ax.set_xticks([i + 1.5 * bar_width for i in index])
    # ax.set_xticklabels(models)
    # ax.legend()
    #
    # plt.show()


    # import matplotlib.pyplot as plt
    #
    # # 指标类型和数据
    # models = ['SRCNN', 'RCAN']
    # set5 = [3.76, 1.29]
    # set14 = [4.37, 2.05]
    # BSD100 = [3.71, 1.56]
    # Urban100 = [9.08, 4.69]
    #
    # # 创建柱状图
    # fig, ax = plt.subplots()
    # bar_width = 0.2
    # index = range(len(models))
    #
    # bar1 = ax.bar(index, set5, bar_width, label='Set5')
    # bar2 = ax.bar([i + bar_width for i in index], set14, bar_width, label='Set14')
    # bar3 = ax.bar([i + 2 * bar_width for i in index], BSD100, bar_width, label='BSD100')
    # bar4 = ax.bar([i + 3 * bar_width for i in index], Urban100, bar_width, label='Urban100')
    #
    #
    # # 添加数据标签
    # def add_labels(bars):
    #     for bar in bars:
    #         height = bar.get_height()
    #         ax.annotate(f'{height:.2f}%',
    #                     xy=(bar.get_x() + bar.get_width() / 2, height),
    #                     xytext=(0, 3),
    #                     textcoords="offset points",
    #                     ha='center', va='bottom')
    #
    #
    # add_labels(bar1)
    # add_labels(bar2)
    # add_labels(bar3)
    # add_labels(bar4)
    #
    # # 添加标签
    # ax.set_xlabel('Models')
    # ax.set_ylabel('Performance Improvement (%)')
    # ax.set_title('SSIM')
    # ax.set_xticks([i + 1.5 * bar_width for i in index])
    # ax.set_xticklabels(models)
    # ax.legend()
    #
    # plt.show()
    #

    # import matplotlib.pyplot as plt
    #
    # # 指标类型和数据
    # models = ['SRCNN', 'RCAN']
    # set5 = [3.84, 1.44]
    # set14 = [4.02, 2.03]
    # BSD100 = [2.74, 1.00]
    # Urban100 = [9.59, 5.07]
    #
    # # 创建柱状图
    # fig, ax = plt.subplots()
    # bar_width = 0.2
    # index = range(len(models))
    #
    # bar1 = ax.bar(index, set5, bar_width, label='Set5')
    # bar2 = ax.bar([i + bar_width for i in index], set14, bar_width, label='Set14')
    # bar3 = ax.bar([i + 2 * bar_width for i in index], BSD100, bar_width, label='BSD100')
    # bar4 = ax.bar([i + 3 * bar_width for i in index], Urban100, bar_width, label='Urban100')
    #
    #
    # # 添加数据标签
    # def add_labels(bars):
    #     for bar in bars:
    #         height = bar.get_height()
    #         ax.annotate(f'{height:.2f}%',
    #                     xy=(bar.get_x() + bar.get_width() / 2, height),
    #                     xytext=(0, 3),
    #                     textcoords="offset points",
    #                     ha='center', va='bottom')
    #
    #
    # add_labels(bar1)
    # add_labels(bar2)
    # add_labels(bar3)
    # add_labels(bar4)
    #
    # # 添加标签
    # ax.set_xlabel('Models')
    # ax.set_ylabel('Performance Improvement (%)')
    # ax.set_title('PSNR')
    # ax.set_xticks([i + 1.5 * bar_width for i in index])
    # ax.set_xticklabels(models)
    # ax.legend()
    #
    # plt.show()
    import matplotlib.pyplot as plt

    # 指标类型和数据
    categories = ['SRCNN', 'RCAN']
    set5 = [0.67, 0.20]
    set14 = [9.85, 0.66]
    BSD100 = [1.37, 0.46]
    Urban100 = [3.94, 1.73]

    # 创建柱状图
    fig, ax = plt.subplots()
    bar_width = 0.15
    index = range(len(categories))

    bar1 = ax.bar(index, set5, bar_width, label='Set5')
    bar2 = ax.bar([i + bar_width for i in index], set14, bar_width, label='Set14')
    bar3 = ax.bar([i + 2 * bar_width for i in index], BSD100, bar_width, label='BSD100')
    bar4 = ax.bar([i + 3 * bar_width for i in index], Urban100, bar_width, label='Urban100')


    # 添加数据标签
    def add_labels(bars):
        for bar in bars:
            height = bar.get_height()
            ax.annotate(f'{height:.2f}%',
                        xy=(bar.get_x() + bar.get_width() / 2, height),
                        xytext=(0, 3),
                        textcoords="offset points",
                        ha='center', va='bottom')


    add_labels(bar1)
    add_labels(bar2)
    add_labels(bar3)
    add_labels(bar4)

    # 添加标签
    ax.set_xlabel('Models')
    ax.set_ylabel('Performance Improvement (%)')
    ax.set_title('SSIM')
    ax.set_xticks([i + 1.5 * bar_width for i in index])
    ax.set_xticklabels(categories)
    ax.legend()

    plt.show()
