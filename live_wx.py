# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

###########################################################################
## Class MyFrame2
###########################################################################

class MyFrame2 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Form Registrasi", pos = wx.DefaultPosition, size = wx.Size( 526,346 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		fgSizer1 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.nama_label = wx.StaticText( self, wx.ID_ANY, u"Nama", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.nama_label.Wrap( -1 )

		fgSizer1.Add( self.nama_label, 0, wx.ALL, 5 )

		self.input_nama = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.input_nama, 0, wx.ALL, 5 )

		self.asal_label = wx.StaticText( self, wx.ID_ANY, u"Asal", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.asal_label.Wrap( -1 )

		fgSizer1.Add( self.asal_label, 0, wx.ALL, 5 )

		self.input_asal = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.input_asal, 0, wx.ALL, 5 )

		self.umur_label = wx.StaticText( self, wx.ID_ANY, u"Umur", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.umur_label.Wrap( -1 )

		fgSizer1.Add( self.umur_label, 0, wx.ALL, 5 )

		self.input_umur = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.input_umur, 0, wx.ALL, 5 )

		self.btn_simpan = wx.Button( self, wx.ID_ANY, u"Simpan", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.btn_simpan, 0, wx.ALL, 5 )


		bSizer1.Add( fgSizer1, 1, wx.EXPAND, 5 )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		self.m_grid1 = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.m_grid1.CreateGrid( 1, 3 )
		self.m_grid1.EnableEditing( True )
		self.m_grid1.EnableGridLines( True )
		self.m_grid1.EnableDragGridSize( False )
		self.m_grid1.SetMargins( 10, 70 )

		# Columns
		self.m_grid1.EnableDragColMove( False )
		self.m_grid1.EnableDragColSize( True )
		self.m_grid1.SetColLabelSize( 30 )
		self.m_grid1.SetColLabelValue( 0, u"Nama" )
		self.m_grid1.SetColLabelValue( 1, u"Asal" )
		self.m_grid1.SetColLabelValue( 2, u"Umur" )
		self.m_grid1.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.m_grid1.EnableDragRowSize( True )
		self.m_grid1.SetRowLabelSize( 80 )
		self.m_grid1.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.m_grid1.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer2.Add( self.m_grid1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		bSizer1.Add( bSizer2, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.btn_simpan.Bind( wx.EVT_BUTTON, self.klik_button )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def klik_button( self, event ):
		event.Skip()


