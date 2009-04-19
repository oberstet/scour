#!/usr/local/bin/python
#  Test Harness for Scour
#
#  Copyright 2009 Jeff Schiller
#
#  This file is part of Scour, http://www.codedread.com/scour/
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

import unittest
import scour
import xml.dom.minidom

SVGNS = 'http://www.w3.org/2000/svg'

# I couldn't figure out how to get ElementTree to work with the following XPath 
# "//*[namespace-uri()='http://example.com']"
# so I decided to use minidom and this helper function that performs a test on a given node 
# and all its children
# func must return either True (if pass) or False (if fail)
def walkTree(elem, func):
	if func(elem) == False:  return False
	for child in elem.childNodes:
		if walkTree(child, func) == False: return False
	return True

class NoInkscapeElements(unittest.TestCase):
	def runTest(self):
		self.assertNotEquals(walkTree(scour.scourXmlFile('unittests/sodipodi.svg').documentElement, 
			lambda e: e.namespaceURI != 'http://www.inkscape.org/namespaces/inkscape'), False,
			'Found Inkscape elements' )

class NoSodipodiElements(unittest.TestCase):
	def runTest(self):
		self.assertNotEquals(walkTree(scour.scourXmlFile('unittests/sodipodi.svg').documentElement, 
			lambda e: e.namespaceURI != 'http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd'), False,
			'Found Sodipodi elements' )

class NoAdobeIllustratorElements(unittest.TestCase):
	def runTest(self):
		self.assertNotEquals(walkTree(scour.scourXmlFile('unittests/adobe.svg').documentElement, 
			lambda e: e.namespaceURI != 'http://ns.adobe.com/AdobeIllustrator/10.0/'), False,
			'Found Adobe Illustrator elements' )
class NoAdobeGraphsElements(unittest.TestCase):
	def runTest(self):
		self.assertNotEquals(walkTree(scour.scourXmlFile('unittests/adobe.svg').documentElement, 
			lambda e: e.namespaceURI != 'http://ns.adobe.com/Graphs/1.0/'), False,
			'Found Adobe Graphs elements' )
class NoAdobeSVGViewerElements(unittest.TestCase):
	def runTest(self):
		self.assertNotEquals(walkTree(scour.scourXmlFile('unittests/adobe.svg').documentElement, 
			lambda e: e.namespaceURI != 'http://ns.adobe.com/AdobeSVGViewerExtensions/3.0/'), False,
			'Found Adobe SVG Viewer elements' )
class NoAdobeVariablesElements(unittest.TestCase):
	def runTest(self):
		self.assertNotEquals(walkTree(scour.scourXmlFile('unittests/adobe.svg').documentElement, 
			lambda e: e.namespaceURI != 'http://ns.adobe.com/Variables/1.0/'), False,
			'Found Adobe Variables elements' )
class NoAdobeSaveForWebElements(unittest.TestCase):
	def runTest(self):
		self.assertNotEquals(walkTree(scour.scourXmlFile('unittests/adobe.svg').documentElement, 
			lambda e: e.namespaceURI != 'http://ns.adobe.com/SaveForWeb/1.0/'), False,
			'Found Adobe Save For Web elements' )
class NoAdobeExtensibilityElements(unittest.TestCase):
	def runTest(self):
		self.assertNotEquals(walkTree(scour.scourXmlFile('unittests/adobe.svg').documentElement, 
			lambda e: e.namespaceURI != 'http://ns.adobe.com/Extensibility/1.0/'), False,
			'Found Adobe Extensibility elements' )
class NoAdobeFlowsElements(unittest.TestCase):
	def runTest(self):
		self.assertNotEquals(walkTree(scour.scourXmlFile('unittests/adobe.svg').documentElement, 
			lambda e: e.namespaceURI != 'http://ns.adobe.com/Flows/1.0/'), False,
			'Found Adobe Flows elements' )
class NoAdobeImageReplacementElements(unittest.TestCase):
	def runTest(self):
		self.assertNotEquals(walkTree(scour.scourXmlFile('unittests/adobe.svg').documentElement, 
			lambda e: e.namespaceURI != 'http://ns.adobe.com/ImageReplacement/1.0/'), False,
			'Found Adobe Image Replacement elements' )
class NoAdobeCustomElements(unittest.TestCase):
	def runTest(self):
		self.assertNotEquals(walkTree(scour.scourXmlFile('unittests/adobe.svg').documentElement, 
			lambda e: e.namespaceURI != 'http://ns.adobe.com/GenericCustomNamespace/1.0/'), False,
			'Found Adobe Custom elements' )
class NoAdobeXPathElements(unittest.TestCase):
	def runTest(self):
		self.assertNotEquals(walkTree(scour.scourXmlFile('unittests/adobe.svg').documentElement, 
			lambda e: e.namespaceURI != 'http://ns.adobe.com/XPath/1.0/'), False,
			'Found Adobe XPath elements' )

class DoNotRemoveMetadataWithOnlyText(unittest.TestCase):
	def runTest(self):
		doc = scour.scourXmlFile('unittests/metadata-with-text.svg')
		self.assertEquals(len(doc.getElementsByTagNameNS(SVGNS, 'metadata')), 1,
			'Removed metadata element with only text child' )

class RemoveEmptyMetadataElement(unittest.TestCase):
	def runTest(self):
		doc = scour.scourXmlFile('unittests/empty-metadata.svg')
		self.assertEquals(len(doc.getElementsByTagNameNS(SVGNS, 'metadata')), 0,
			'Did not remove empty metadata element' )

class RemoveEmptyGElements(unittest.TestCase):
	def runTest(self):
		doc = scour.scourXmlFile('unittests/empty-g.svg')
		self.assertEquals(len(doc.getElementsByTagNameNS(SVGNS, 'g')), 1,
			'Did not remove empty g element' )

class RemoveUnreferencedPattern(unittest.TestCase):
	def runTest(self):
		doc = scour.scourXmlFile('unittests/unreferenced-pattern.svg')
		self.assertEquals(len(doc.getElementsByTagNameNS(SVGNS, 'pattern')), 0,
			'Unreferenced pattern not removed' )

class RemoveUnreferencedLinearGradient(unittest.TestCase):
	def runTest(self):
		doc = scour.scourXmlFile('unittests/unreferenced-linearGradient.svg')
		self.assertEquals(len(doc.getElementsByTagNameNS(SVGNS, 'linearGradient')), 0,
			'Unreferenced linearGradient not removed' )

class RemoveUnreferencedRadialGradient(unittest.TestCase):
	def runTest(self):
		doc = scour.scourXmlFile('unittests/unreferenced-radialGradient.svg')
		self.assertEquals(len(doc.getElementsByTagNameNS(SVGNS, 'radialradient')), 0,
			'Unreferenced radialGradient not removed' )

class RemoveUselessNestedGroups(unittest.TestCase):
	def runTest(self):
		doc = scour.scourXmlFile('unittests/nested-useless-groups.svg')
		self.assertEquals(len(doc.getElementsByTagNameNS(SVGNS, 'g')), 1,
			'Useless nested groups not removed' )

class RemoveDuplicateLinearGradientStops(unittest.TestCase):
	def runTest(self):
		doc = scour.scourXmlFile('unittests/duplicate-gradient-stops.svg')
		grad = doc.getElementsByTagNameNS(SVGNS, 'linearGradient')
		self.assertEquals(len(grad[0].getElementsByTagNameNS(SVGNS, 'stop')), 3,
			'Duplicate linear gradient stops not removed' )

class RemoveDuplicateRadialGradientStops(unittest.TestCase):
	def runTest(self):
		doc = scour.scourXmlFile('unittests/duplicate-gradient-stops.svg')
		grad = doc.getElementsByTagNameNS(SVGNS, 'radialGradient')
		self.assertEquals(len(grad[0].getElementsByTagNameNS(SVGNS, 'stop')), 3,
			'Duplicate radial gradient stops not removed' )

class NoSodipodiNamespaceDecl(unittest.TestCase):
	def runTest(self):
		attrs = scour.scourXmlFile('unittests/sodipodi.svg').documentElement.attributes
		for i in range(len(attrs)):
			self.assertNotEquals(attrs.item(i).nodeValue,
				'http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd',
				'Sodipodi namespace declaration found' )

class NoInkscapeNamespaceDecl(unittest.TestCase):
	def runTest(self):
		attrs = scour.scourXmlFile('unittests/inkscape.svg').documentElement.attributes
		for i in range(len(attrs)):
			self.assertNotEquals(attrs.item(i).nodeValue,
				'http://www.inkscape.org/namespaces/inkscape',
				'Inkscape namespace declaration found' )
		
class NoSodipodiAttributes(unittest.TestCase):
	def runTest(self):	
		def findSodipodiAttr(elem):
			attrs = elem.attributes
			if attrs == None: return True
			for i in range(len(attrs)):
				if attrs.item(i).namespaceURI == 'http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd':
					return False
			return True
		self.assertNotEquals(walkTree(scour.scourXmlFile('unittests/sodipodi.svg').documentElement, 
			findSodipodiAttr), False,
			'Found Sodipodi attributes' )
			
class NoInkscapeAttributes(unittest.TestCase):
	def runTest(self):	
		def findInkscapeAttr(elem):
			attrs = elem.attributes
			if attrs == None: return True
			for i in range(len(attrs)):
				if attrs.item(i).namespaceURI == 'http://www.inkscape.org/namespaces/inkscape':
					return False
			return True
		self.assertNotEquals(walkTree(scour.scourXmlFile('unittests/inkscape.svg').documentElement, 
			findInkscapeAttr), False,
			'Found Inkscape attributes' )

class KeepReferencedFonts(unittest.TestCase):
	def runTest(self):
		doc = scour.scourXmlFile('unittests/referenced-font.svg')
		fonts = doc.documentElement.getElementsByTagNameNS('http://www.w3.org/2000/svg','font')
		self.assertEquals(len(fonts), 1,
			"Font wrongly removed from <defs>" )

#class RemoveUnreferencedFonts(unittest.TestCase):
#	def runTest(self):
#		doc = scour.scourXmlFile('unittests/unreferenced-font.svg')
#		fonts = doc.documentElement.getElementsByTagNameNS('http://www.w3.org/2000/svg','font')
#		self.assertEquals(len(fonts), 0,
#			"Font was not removed from <defs>" )
		
if __name__ == '__main__':
    unittest.main()
