import pyjd
pyjd.setup("./public/GChartTestApp.html")

from pyjamas import DeferredCommand
from pyjamas.ui.HTML import HTML
from pyjamas.ui.RootPanel import RootPanel
from pyjamas.chart import GChart

from pyjamas.Canvas.GWTCanvas import GWTCanvas

from TestGChart00 import TestGChart00 
from TestGChart01 import TestGChart01 
from TestGChart02 import TestGChart02 

from TestGChart05 import TestGChart05 

from GChartExample00 import GChartExample00 
from GChartExample00a import GChartExample00a
from GChartExample01 import GChartExample01 
from GChartExample02 import GChartExample02
from GChartExample03 import GChartExample03
from GChartExample04 import GChartExample04

from GChartExample06 import GChartExample06
from GChartExample07 import GChartExample07


from GChartExample14 import GChartExample14

from GChartExample17 import GChartExample17

from GChartExample20 import GChartExample20
from GChartExample21 import GChartExample21

from GChartExample24 import GChartExample24
from GChartExample25 import GChartExample25

"""*
*
* Displays the test  chart in the browser, and checks the HTML
* generated against previous, visually validated, browser
* output HTML hash codes to see if HTML output from the test
* has changed (possibly due to an error).
*
* As long as GChart and the test set itself has not changed,
* these tests can be performed by first running in hosted
* mode, then clicking on the "Compile/Browse" button. If
* "Test passed" is displayed in hosted mode and also in
* Firefox after the compile (this assumes Firefox is your default browser)
* it means that the generated HTML has not changed since
* the last time it was visually inspected--test passed.
*
* If the test or GChart changes so as to change browser output,
* you will have to visually verify the charts, and then (assuming the
* charts are correct) enter the hashcodes.
*
* In the most common case where the test and output are unchanged,
* the test should go through very quickly.
*
"""
    
""" Linear congruent random number generator.
*
* Cannot use GWT's Math.random() because, for automated
* testing, we require that the exact same random sequence
* be used each time (GWT does not support the JDK's more
* generic Random class, which would have allowed this).
*
* Constants are from Knuth via Numerical Recipes in C.
*
"""
i = 0
def rnd():
    m = 217728
    a = 84589
    c = 45989
    i = (a*i + c) % m
    return i/m


"""
* Allows us to quickly check if test charts changed since last time
* they were manually inspected, thus eliminating the many tedious
* re-inspections I used to have to do.
*
* Whenever the test changes, or GChart changes in a way that changes
* generated HTML, manual chart re-inspection is needed and
* the various hashcodes below need to be re-entered.
*
* Note that sometimes the hosted mode cold-start hash code is generated by
* a refresh, so if you get the same hash code the first time
* you press refresh, try again to produce the second, refresh, hash code.
*
* Note, that if you open the compiled app directly from the file system
* rather than via the Compile/Browse button, Firefox produces a different
* HTML/hash code, so you must run the test via the Compile/Browse button.
*
"""
 
from GChartTestAppUtil import getTitle

class AddOneChart:
    def __init__(self, gchart, needsUpdate=True):
        #gchart.setOptimizeForMemory(True)
        self.gchart = gchart
        self.needsUpdate = needsUpdate
    
    def execute(self):
        RootPanel().get("testappcharts").add(HTML(getTitle(self.gchart)))
        RootPanel().get("testappcharts").add(self.gchart)
        if self.needsUpdate:
            self.gchart.update()
        



def addChart(gchart):
    DeferredCommand.add(AddOneChart(gchart, True))

def addChartNoUpdate(gchart):
    DeferredCommand.add(AddOneChart(gchart, False))

class GWTCanvasBasedCanvasFactory(object):
    def create(self):
        return GWTCanvas()


def onModuleLoad():
    
    # TODO: port http://code.google.com/p/gwt-canvas
    GChart.setCanvasFactory(GWTCanvasBasedCanvasFactory())
    
    # thinking about retiring these tests:
    #    addChart(GChartExample11(0,2,False))
    #    addChart(GChartExample11(0,3,False))
    #    addChart(GChartExample11(0,4,False))
    #    addChart(GChartExample11(0,5,False))
    #    addChart(GChartExample11(0,6,False))
    #    addChart(GChartExample11(0,7,False))
    #    addChart(GChartExample11(0,8,False))
    #    addChart(TestGChart40())
    #    DeferredCommand.add(Command() { void execute() {
    #    RootPanel.get().add(TestGChart41a())
    #  }})
    
    # To focus on a single test, simply use Eclipse's Source, Toggle comment
    #addChart(GChartExample00())
    #addChart(GChartExample00a())
    #    addChart(GChartExample00b())
    #    addChart(GChartExample00c())
    #addChart(GChartExample01())
    #    addChart(GChartExample01a(3))
    #    addChart(GChartExample01a(0))
    #    addChart(GChartExample01b())
    #    addChart(GChartExample01c())
    #addChart(GChartExample02())
    #addChart(GChartExample03())
    #addChart(GChartExample04())
    #    addChart(GChartExample04a())
    #    addChart(GChartExample04b())
    #    addChart(GChartExample05())
    #addChart(GChartExample06())
    addChart(GChartExample07())
    #    addChart(GChartExample08())
    #    addChart(GChartExample09())
    #    addChart(GChartExample10())
    #    addChart(GChartExample11(0,1,True))
    #    addChart(GChartExample11(0,1,False))
    #    addChart(GChartExample11(1,1,False))
    #    addChart(GChartExample11(2,1,False))
    #    addChart(GChartExample11(3,1,False))
    #    addChart(GChartExample12())
    #addChart(GChartExample14())
    #    addChart(GChartExample15())
    #    addChart(GChartExample15a())
    #    addChart(GChartExample15b())
    #    addChart(GChartExample16())
    #addChart(GChartExample17())
    #      addChart(GChartExample17a())
    #      addChart(GChartExample18())
    #      addChart(GChartExample18a())
    #      addChart(GChartExample19())
    addChart(GChartExample20())
    #      addChart(GChartExample20a())
    #addChart(GChartExample21())
    #      addChart(GChartExample22())
    #      addChart(GChartExample22a())
    #      addChart(GChartExample23(False, False))
    #      addChart(GChartExample23(False, True))
    #      addChart(GChartExample23(True, False))
    #      addChart(GChartExample23(True, True))
    #addChart(GChartExample24())
    #addChart(GChartExample25())
    #DeferredCommand.add(Command() {
    #    def execute(self):
    #        RootPanel.get().add(GChartExample25())
    #    
    #)
    #    addChart(TestGChart00())
    #addChartNoUpdate(TestGChart01(0,0))
    #addChartNoUpdate(TestGChart01(1,0))
    #addChartNoUpdate(TestGChart01(2,0))
    #addChartNoUpdate(TestGChart01(3,0))
    #    addChartNoUpdate(TestGChart01(0,1))
    #    addChartNoUpdate(TestGChart01(1,1))
    #    addChartNoUpdate(TestGChart01(2,1))
    #    addChartNoUpdate(TestGChart01(3,1))
    #    addChartNoUpdate(TestGChart01(0,2))
    #    addChartNoUpdate(TestGChart01(1,2))
    #    addChartNoUpdate(TestGChart01(2,2))
    #    addChartNoUpdate(TestGChart01(3,2))
    #    addChart(TestGChart01a())
    #addChart(TestGChart02())
    #    addChart(TestGChart03())
    #    addChart(TestGChart04())
    #    addChart(TestGChart04a())
    #addChart(TestGChart05(False))
    addChart(TestGChart05(True))
    #    addChart(TestGChart06(False))
    #    addChart(TestGChart06(True))
    #    addChart(TestGChart07(0,0,10,1))
    #    addChart(TestGChart07(10,0,10,1))
    #    addChart(TestGChart07(-10,0,10,1))
    #    addChart(TestGChart07(0,10,10,1))
    #    addChart(TestGChart07(0,-10,10,1))
    #    addChart(TestGChart07(0,0,30,1))
    #    addChart(TestGChart07(0,0,10,3))
    #    addChart(TestGChart07(0,0,10,-1))
    #    addChart(TestGChart07(0,0,10,-2))
    #    addChart(TestGChart07(0,0,10,-3))
    #    addChart(TestGChart07a())
    #    addChart(TestGChart08())
    #    addChart(TestGChart09())
    #    addChart(TestGChart10())
    #    addChart(TestGChart11())
    #    addChart(TestGChart12())
    #    addChart(TestGChart14())
    #    addChart(TestGChart14a())
    #    addChart(TestGChart14b())
    #    addChart(TestGChart14c())
    #    addChart(TestGChart14d())
    #    addChart(TestGChart15(1))
    #    addChart(TestGChart15(0))
    #    addChart(TestGChart16(0,1))
    #    addChart(TestGChart16(1,1))
    #    addChart(TestGChart16(2,1))
    #    addChart(TestGChart16(3,1))
    #    addChart(TestGChart16(4,1))
    #    addChart(TestGChart16(5,1))
    #    addChart(TestGChart16(0,10))
    #    addChart(TestGChart16(1,10))
    #    addChart(TestGChart16(2,10))
    #    addChart(TestGChart16(3,10))
    #    addChart(TestGChart16(4,10))
    #    addChart(TestGChart16(5,10))
    #    addChart(TestGChart17())
    #    addChart(TestGChart17a())
    #    addChart(TestGChart17b())
    #    addChart(TestGChart18())
    #    addChart(TestGChart19(0))
    #    addChart(TestGChart19(1))
    #    addChart(TestGChart19(2))
    #    addChart(TestGChart19(3))
    #    addChart(TestGChart20())
    #    addChart(TestGChart20a())
    #    # extra layer to stop "this script is taking too long" browser msg
    #    DeferredCommand.add(Command() < void execute() <
    #    addChart(TestGChart21())
    #    addChart(TestGChart22(False))
    #    addChart(TestGChart22(True))
    #    addChart(TestGChart23(1))
    #    addChart(TestGChart23(2))
    #    addChart(TestGChart23(3))
    #    addChart(TestGChart24(1))
    #    addChart(TestGChart24(2))
    #    addChart(TestGChart25(8,1,1,1,20,20))
    #    addChart(TestGChart25(8,2,2,1,1,1))
    #    addChart(TestGChart25(8,5,5,1,0,0))
    #    addChart(TestGChart25(8,1,1,.5,10,10))
    #    addChart(TestGChart25(8,2,2,.5,10,10))
    #    addChart(TestGChart25(8,4,4,.5,10,10))
    #    addChart(TestGChart25(8,8,8,.5,10,10))
    #    addChart(TestGChart25(8,1,1,1.5,20,20))
    #    addChart(TestGChart25b(8,1,0,1.5,20,20))
    #    addChart(TestGChart25b(8,5,5,1,0,0))
    #    addChart(TestGChart26())
    #    addChart(TestGChart27())
    #    addChart(TestGChart28(False, 1, False))
    #    addChart(TestGChart28(True, 1, False))
    #    addChart(TestGChart28(False, 2, False))
    #    addChart(TestGChart28(True, 2, False))
    #    addChart(TestGChart28(False, 4, False))
    #    addChart(TestGChart28(True, 4, False))
    #
    #    addChart(TestGChart28(False, 1, True))
    #    addChart(TestGChart28(True, 1, True))
    #    addChart(TestGChart28(False, 2, True))
    #    addChart(TestGChart28(True, 2, True))
    #    addChart(TestGChart28(False, 4, True))
    ## Hover testing charts start here
    #    addChart(TestGChart28(True, 4, True))
    #    addChart(TestGChart29())
    #    addChart(TestGChart30(False, False))
    #    addChart(TestGChart30(True, False))
    #    addChart(TestGChart30(False, True))
    #    addChart(TestGChart30(True, True))
    #    addChart(TestGChart31())
    #    addChart(TestGChart32())
    ## Not a GCchart, a ScrollPanel that contains a Gchart:
    #    DeferredCommand.add(Command() < void execute() <
    #      RootPanel.get().add(TestGChart33())
    #    >>)
    #     addChart(TestGChart34())
    #     addChart(TestGChart35())
    #      addChart( TestGChart36(GChart.TouchedPointUpdateOption.TOUCHED_POINT_CLEARED))
    #      addChart(TestGChart36(GChart.TouchedPointUpdateOption.TOUCHED_POINT_LOCKED))
    #      addChart(TestGChart36(GChart.TouchedPointUpdateOption.TOUCHED_POINT_UPDATED))
    #        addChart(TestGChart37(GChart.TouchedPointUpdateOption.TOUCHED_POINT_CLEARED))
    #        addChart(TestGChart37(GChart.TouchedPointUpdateOption.TOUCHED_POINT_LOCKED))
    #        addChart(TestGChart37(GChart.TouchedPointUpdateOption.TOUCHED_POINT_UPDATED))
    #        addChart(TestGChart38(GChart.TouchedPointUpdateOption.TOUCHED_POINT_CLEARED))
    #        addChart(TestGChart38(GChart.TouchedPointUpdateOption.TOUCHED_POINT_LOCKED))
    #        addChart(TestGChart38(GChart.TouchedPointUpdateOption.TOUCHED_POINT_UPDATED))
    #        addChart(TestGChart39())
    #        DeferredCommand.add(Command() < void execute() <
    #            RootPanel.get().add(TestGChart41())
    #        >>)
    #        DeferredCommand.add(Command() < void execute() <
    #            RootPanel.get().add(TestGChart41a())
    #        >>)
    #      addChart(TestGChart42())
    #      addChart(TestGChart43())
    #      addChart(TestGChart44())
    #        addChart(TestGChart45(0))
    #      addChart(TestGChart45(1))
    #    	addChart(TestGChart45(2))
    #      addChart(TestGChart45(3))
    #      addChart(TestGChart45(4))
    #      DeferredCommand.add(Command() < void execute() <
    #      RootPanel.get().add(TestGChart46())
    #  >>)
    #      addChart(TestGChart47(0,1,5))
    #      addChart(TestGChart47(1,1,5))
    #      addChart(TestGChart47(2,1,5))
    #      addChart(TestGChart47(3,1,5))
    #      addChart(TestGChart47(4,1,5))
    #      addChart(TestGChart47(5,1,5))
    #      addChart(TestGChart47(6,1,5))
    #      addChart(TestGChart47(7,1,5))
    #      addChart(TestGChart47(0,0,2))
    #      addChart(TestGChart47(1,0,2))
    #      addChart(TestGChart47(2,0,2))
    #      addChart(TestGChart47(3,0,2))
    #      addChart(TestGChart47(4,0,2))
    #      addChart(TestGChart47(5,0,2))
    #      addChart(TestGChart47(6,0,2))
    #      addChart(TestGChart47(7,0,2))
    #      addChart(TestGChart47(0,1,3))
    #      addChart(TestGChart47(1,1,3))
    #      addChart(TestGChart47(2,1,3))
    #      addChart(TestGChart47(3,1,3))
    #      addChart(TestGChart47(4,1,3))
    #      addChart(TestGChart47(5,1,3))
    #      addChart(TestGChart47(6,1,3))
    #      addChart(TestGChart47(7,1,3))
    #      addChart(TestGChart47(8,3,5))
    #      addChart(TestGChart47(9,3,5))
    #      addChart(TestGChart48(3))
    #      addChart(TestGChart48(4))
    #      addChart(TestGChart48(5))
    #      addChart(TestGChart48(6))
    #      addChart(TestGChart48(8))
    #      addChart(TestGChart48(9))
    #      addChart(TestGChart48(10))
    #      addChart(TestGChart49(3,False, False))
    #      addChart(TestGChart49(3, False, True))
    #      addChart(TestGChart49(3,True, False))
    #      addChart(TestGChart49(3, True, True))
    #      addChart(TestGChart50(GChart.TickLocation.CENTERED,0))
    #      addChart(TestGChart50(GChart.TickLocation.INSIDE,0))
    #      addChart(TestGChart50(GChart.TickLocation.OUTSIDE,0))
    #      addChart(TestGChart50(GChart.TickLocation.CENTERED,5))
    #      addChart(TestGChart50(GChart.TickLocation.INSIDE,5))
    #      addChart(TestGChart50(GChart.TickLocation.OUTSIDE,5))
    #      addChart(TestGChart51(0))
    #      addChart(TestGChart51(1))
    #      addChart(TestGChart52())
    #      addChart(TestGChart53())
    #    >>)
    #    addChart(TestGChart54())
    #  DeferredCommand.add(Command() < void execute() <
    #      RootPanel.get().add(TestGChart55())
    #  >>)
    #  DeferredCommand.add(Command() < void execute() <
    #      RootPanel.get().add(TestGChart55a())
    #  >>)
    #  addChart(TestGChart56())
    #
    #addChart(TestGChart57())
    #RootPanel.get().add(TestGChart57a())
    #RootPanel.get().add(TestGChart58())

    #addChart(TestGChart00())
    
    RootPanel().get("loadingMessage").setVisible(False)
    
    
    
    

onModuleLoad()
pyjd.run()
