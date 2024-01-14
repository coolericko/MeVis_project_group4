from mevis import *

# LUT
def lutSelected():
  ctx.field('SoLUTEditor2D.lutListItem').value = ctx.control('lutListView').currentItem().text(0)
  
def lutRenamed(item,column,newvalue):
  ctx.field('newLutName').value = newvalue
  ctx.field('lutNameChanged').touch()
  
def tagSelected():
  result = []
  for id in ctx.control('tagListView').selectedItemIds():
    result.append(ctx.control('tagListView').itemForId(id).text(0))
  ctx.field('SoLUTEditor2D.tagListItems').value = '[' + (','.join(result)) + ']'
  
  
def CSOSelected():
  ctx.field('CSOManager.CSOListItem').value = ctx.control('CSOListView').currentItem().text(0)
  
  
  
# CSO Manager
def updateCSOListView(field=None):
  listView = ctx.control("csoListView")
  alreadyCalledLater = listView.property("listNeedsUpdate") or listView.property("selectionNeedsUpdate")
  if not alreadyCalledLater:
    ctx.callLater(0, "updateCSOListViewLater")
  listView.setProperty("listNeedsUpdate", True)
  
def updateCSOListViewSelection(field=None):
  listView = ctx.control("csoListView")
  alreadyCalledLater = listView.property("listNeedsUpdate") or listView.property("selectionNeedsUpdate")
  if not alreadyCalledLater:
    ctx.callLater(0, "updateCSOListViewLater")
  listView.setProperty("selectionNeedsUpdate", True)
  
def updateCSOListViewLater():  
  listView = ctx.control("csoListView")
  if listView.property("listNeedsUpdate"):
    listView.setProperty("listNeedsUpdate", None)
    buildCSOListView()
  listView.setProperty("selectionNeedsUpdate", None)
  csoSelectionChanged()
  
def build():
  csoDisplayTree = ctx.field("CSOManager.csoDisplayTree").stringValue()
  csoStrings = csoDisplayTree.split("|")