import matplotlib.pyplot as plt

def plot_images2(data,figsize=(10,6)):
    rows = len(data)
    cols = len(data[0])
    print(cols,rows)
    fig ,ax = plt.subplots(cols,rows,figsize=figsize)
    for r in range(rows):
        if len(data[r]) != cols:
            print(len(data[r]),'!=',rows)
            break
        for c in range(cols):
            ax[c,r].imshow(data[r][c])
    return fig,ax
