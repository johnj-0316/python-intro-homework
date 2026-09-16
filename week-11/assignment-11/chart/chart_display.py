from matplotlib import pyplot

# title is: How frequent does the chosen type appear as the 1st and 2nd slot for all pokemon?

def chart_display(title: str, categories: list[str], quantities: list[int]):
    figure, axis = pyplot.subplots(figsize=(7, 5))
    bars = axis.bar(categories, quantities, color='#2171B5', edgecolor='black', width=0.6)
    axis.bar_label(bars, padding=3)
    axis.set_title(title, fontsize=14, fontweight='bold', pad=15)
    axis.set_xlabel('Slot Types', fontsize=12)
    axis.set_ylabel('Slot Frequencies', fontsize=12)
    pyplot.tight_layout()
    pyplot.show()