# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class SwitchFrame
###########################################################################

class SwitchFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Switch discovery", pos = wx.DefaultPosition, size = wx.Size( 452,348 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		SelectInterface = wx.GridSizer( 4, 2, 0, 0 )

		self.interface_label = wx.StaticText( self, wx.ID_ANY, u"Network interface", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.interface_label.Wrap( -1 )

		SelectInterface.Add( self.interface_label, 0, wx.ALL, 5 )

		interface_selectChoices = []
		self.interface_select = wx.Choice( self, wx.ID_ANY, wx.Point( -1,-1 ), wx.DefaultSize, interface_selectChoices, 0 )
		self.interface_select.SetSelection( 0 )
		self.interface_select.SetToolTip( u"Select network interface" )

		SelectInterface.Add( self.interface_select, 0, wx.ALL, 5 )

		self.interface_ip_label = wx.StaticText( self, wx.ID_ANY, u"IP address:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.interface_ip_label.Wrap( -1 )

		SelectInterface.Add( self.interface_ip_label, 0, wx.ALL, 5 )

		self.interface_ip = wx.StaticText( self, wx.ID_ANY, u"Dummy", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.interface_ip.Wrap( -1 )

		SelectInterface.Add( self.interface_ip, 0, wx.ALL, 5 )

		self.interface_mac_label = wx.StaticText( self, wx.ID_ANY, u"MAC address", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.interface_mac_label.Wrap( -1 )

		SelectInterface.Add( self.interface_mac_label, 0, wx.ALL, 5 )

		self.interface_mac = wx.StaticText( self, wx.ID_ANY, u"Dummy", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.interface_mac.Wrap( -1 )

		SelectInterface.Add( self.interface_mac, 0, wx.ALL, 5 )

		self.load_button = wx.Button( self, wx.ID_ANY, u"Discover", wx.DefaultPosition, wx.DefaultSize, 0 )
		SelectInterface.Add( self.load_button, 0, wx.ALL, 5 )


		bSizer2.Add( SelectInterface, 1, wx.EXPAND|wx.ALL, 5 )

		self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL, u"test" )
		gSizer2 = wx.GridSizer( 0, 2, 0, 0 )

		SwitchInfo = wx.GridSizer( 0, 2, 0, 0 )

		self.switch_name_label = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Switch name:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.switch_name_label.Wrap( -1 )

		SwitchInfo.Add( self.switch_name_label, 0, wx.ALL, 5 )

		self.switch_name = wx.StaticText( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.switch_name.Wrap( -1 )

		SwitchInfo.Add( self.switch_name, 0, wx.ALL, 5 )

		self.switch_model_label = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Switch model:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.switch_model_label.Wrap( -1 )

		SwitchInfo.Add( self.switch_model_label, 0, wx.ALL, 5 )

		self.switch_model = wx.StaticText( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.switch_model.Wrap( -1 )

		SwitchInfo.Add( self.switch_model, 0, wx.ALL, 5 )

		self.switch_ip_label = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Switch IP:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.switch_ip_label.Wrap( -1 )

		SwitchInfo.Add( self.switch_ip_label, 0, wx.ALL, 5 )

		self.switch_ip = wx.StaticText( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.switch_ip.Wrap( -1 )

		SwitchInfo.Add( self.switch_ip, 0, wx.ALL, 5 )


		gSizer2.Add( SwitchInfo, 1, wx.EXPAND, 5 )

		PortInfo = wx.GridSizer( 0, 2, 0, 0 )

		self.port_label = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Interface:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.port_label.Wrap( -1 )

		PortInfo.Add( self.port_label, 0, wx.ALL, 5 )

		self.port = wx.StaticText( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.port.Wrap( -1 )

		PortInfo.Add( self.port, 0, wx.ALL, 5 )

		self.vlan_label = wx.StaticText( self.m_panel1, wx.ID_ANY, u"VLAN:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.vlan_label.Wrap( -1 )

		PortInfo.Add( self.vlan_label, 0, wx.ALL, 5 )

		self.vlan = wx.StaticText( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.vlan.Wrap( -1 )

		PortInfo.Add( self.vlan, 0, wx.ALL, 5 )

		self.m_staticText24 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText24.Wrap( -1 )

		PortInfo.Add( self.m_staticText24, 0, wx.ALL, 5 )


		gSizer2.Add( PortInfo, 1, wx.EXPAND, 5 )


		self.m_panel1.SetSizer( gSizer2 )
		self.m_panel1.Layout()
		gSizer2.Fit( self.m_panel1 )
		bSizer2.Add( self.m_panel1, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer2 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.interface_select.Bind( wx.EVT_CHOICE, self.setInterface )
		self.load_button.Bind( wx.EVT_BUTTON, self.discoverSwitches )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def setInterface( self, event ):
		pass

	def discoverSwitches( self, event ):
		pass


