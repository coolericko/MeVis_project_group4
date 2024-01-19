from mevis import *


# LUT
def lutSelected():
    ctx.field("SoLUTEditor2D.lutListItem").value = (
        ctx.control("lutListView").currentItem().text(0)
    )


def lutRenamed(item, column, newvalue):
    ctx.field("newLutName").value = newvalue
    ctx.field("lutNameChanged").touch()


def tagSelected():
    result = []
    for id in ctx.control("tagListView").selectedItemIds():
        result.append(ctx.control("tagListView").itemForId(id).text(0))
    ctx.field("SoLUTEditor2D.tagListItems").value = "[" + (",".join(result)) + "]"