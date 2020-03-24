"""
https://www.hackerrank.com/challenges/designer-pdf-viewer/
"""
def designerPdfViewer(h, word):
    height = 0
    for c in word:
        if h[ord(c) - 97] > height:
            height = h[ord(c) - 97]
    return len(word) * height
