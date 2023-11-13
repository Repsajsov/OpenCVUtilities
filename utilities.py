import numpy as np
import cv2
import matplotlib.pyplot as plt


class Utilities:
    @staticmethod
    def read_images(*images, cvtColor_code=cv2.COLOR_BGR2RGB):
        result = [cv2.cvtColor(cv2.imread(image), cvtColor_code) for image in images]
        return result if len(result) > 1 else result[0]

    @staticmethod
    def show_images(*images, cmap="gray", figsize=(12, 12)):
        n = len(images)
        if n == 1:
            fig, axis = plt.subplots(figsize=figsize)
            axis.imshow(images[0], cmap=cmap)
        elif n == 2:
            fig, axis = plt.subplots(ncols=2, figsize=figsize)
            axis[0].imshow(images[0], cmap=cmap)
            axis[1].imshow(images[1], cmap=cmap)

        else:
            columns = int(np.ceil(np.sqrt(n)))
            rows = int(np.ceil(n / columns))

            fig, axis = plt.subplots(rows, columns, figsize=figsize)

            k = 0
            for i in range(rows):
                for j in range(columns):
                    if k < n:
                        axis[i][j].imshow(images[k], cmap=cmap)
                        k += 1
                    else:
                        axis[i][j].axis("off")

        plt.tight_layout()
        plt.show()
        return fig, axis
