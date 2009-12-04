"""
PureMVC Python Demo - wxPython Employee Admin 
By Toby de Havilland <toby.de.havilland@puremvc.org>
Copyright(c) 2007-08 Toby de Havilland, Some rights reserved.
Addapted for pyjamas: Kees Bos
"""

import puremvc.interfaces
import puremvc.patterns.mediator

import model, consts, EmployeeAdmin, vo

from pyjamas.Window import alert

class DialogMediator(puremvc.patterns.mediator.Mediator, puremvc.interfaces.IMediator):
    
    NAME = 'DialogMediator'
    
    def __init__(self, viewComponent):
        super(DialogMediator, self).__init__(DialogMediator.NAME, viewComponent)
        self.viewComponent.mediator = self

    def listNotificationInterests(self):
        return [
        EmployeeAdmin.AppFacade.SHOW_DIALOG,
        ]

    def handleNotification(self, note):
        try:
            noteName = note.getName()
            if noteName == EmployeeAdmin.AppFacade.SHOW_DIALOG:
                alert(note.getBody())
        except:
            raise

class UserFormMediator(puremvc.patterns.mediator.Mediator, puremvc.interfaces.IMediator):
    
    NAME = 'UserFormMediator'
    
    userProxy = None
    
    def __init__(self, viewComponent):
        super(UserFormMediator, self).__init__(UserFormMediator.NAME, viewComponent)
        self.viewComponent.mediator = self
        self.viewComponent.addBtn.addClickListener(self.onAdd)
        self.viewComponent.cancelBtn.addClickListener(self.onCancel)
        
        self.userProxy = self.facade.retrieveProxy(model.UserProxy.NAME)
        self.viewComponent.updateDepartmentCombo(consts.DeptList, consts.DEPT_NONE_SELECTED)
        
    def listNotificationInterests(self):
        return [
        EmployeeAdmin.AppFacade.NEW_USER,
        EmployeeAdmin.AppFacade.USER_DELETED,
        EmployeeAdmin.AppFacade.USER_SELECTED
        ]

    def handleNotification(self, note): 
        try:
            noteName = note.getName()
            if noteName == EmployeeAdmin.AppFacade.NEW_USER:
                self.viewComponent.updateMode(self.viewComponent.MODE_ADD)
                self.clearForm()
                self.viewComponent.firstInput.setFocus(True)
            
            if noteName == EmployeeAdmin.AppFacade.USER_DELETED:
                self.viewComponent.user = None
                self.clearForm()
                
            if noteName == EmployeeAdmin.AppFacade.USER_SELECTED:
                user = note.getBody()
                if not user:
                    self.clearForm()
                else:
                    self.viewComponent.updateUser(note.getBody())
                    self.viewComponent.updateMode(self.viewComponent.MODE_EDIT)
        except:
            raise
    
    def clearForm(self):
        self.viewComponent.user = None
        self.viewComponent.usernameInput.setText('')
        self.viewComponent.firstInput.setText('')
        self.viewComponent.lastInput.setText('')
        self.viewComponent.emailInput.setText('')
        self.viewComponent.passwordInput.setText('')
        self.viewComponent.confirmInput.setText('')
        self.viewComponent.departmentCombo.setItemTextSelection(None)
    
    def onAdd(self, evnt):
        if self.viewComponent.mode == self.viewComponent.MODE_ADD:
            self.addUser()
        else:
            self.updateUser()

    def addUser(self):
        l = self.viewComponent.departmentCombo.getSelectedItemText(True)
        l = l and l[0] or None
        user = vo.UserVO(self.viewComponent.usernameInput.getText(), 
                         self.viewComponent.firstInput.getText(), 
                         self.viewComponent.lastInput.getText(), 
                         self.viewComponent.emailInput.getText(), 
                         self.viewComponent.passwordInput.getText(),
                         l)
        self.viewComponent.user = user
        self.userProxy.addItem(user)
        self.sendNotification(EmployeeAdmin.AppFacade.USER_ADDED, user)
        self.clearForm()

    def updateUser(self):
        l = self.viewComponent.departmentCombo.getSelectedItemText(True)
        l = l and l[0] or None
        user = vo.UserVO(self.viewComponent.usernameInput.getText(), 
                         self.viewComponent.firstInput.getText(), 
                         self.viewComponent.lastInput.getText(), 
                         self.viewComponent.emailInput.getText(), 
                         self.viewComponent.passwordInput.getText(),
                         l)
        self.viewComponent.user = user
        self.userProxy.updateItem(user)
        self.sendNotification(EmployeeAdmin.AppFacade.USER_UPDATED, user)
        self.clearForm()

    def onCancel(self, evnt):
        self.sendNotification(EmployeeAdmin.AppFacade.CANCEL_SELECTED)
        self.clearForm()

class UserListMediator(puremvc.patterns.mediator.Mediator, puremvc.interfaces.IMediator):

    NAME = 'UserListMediator'
    
    userProxy = None

    def __init__(self, viewComponent):
        super(UserListMediator, self).__init__(UserListMediator.NAME, viewComponent)
        self.viewComponent.newBtn.addClickListener(self.onNewUser)
        self.viewComponent.deleteBtn.addClickListener(self.onDeleteUser)
        self.viewComponent.userGrid.addTableListener(self.onSelectUser)
        
        self.userProxy = self.facade.retrieveProxy(model.UserProxy.NAME)
        self.viewComponent.updateUserGrid(self.userProxy.getUsers())
        
    def listNotificationInterests(self):
        return [
        EmployeeAdmin.AppFacade.CANCEL_SELECTED,
        EmployeeAdmin.AppFacade.USER_UPDATED,
        EmployeeAdmin.AppFacade.USER_ADDED,
        EmployeeAdmin.AppFacade.USER_DELETED
        ]

    def handleNotification(self, note):
        try:
            noteName = note.getName()
            self.viewComponent.deSelect()
            if noteName == EmployeeAdmin.AppFacade.CANCEL_SELECTED:
                self.viewComponent.deSelect()
                self.viewComponent.updateUserGrid(self.userProxy.getUsers())
            
            elif noteName == EmployeeAdmin.AppFacade.USER_UPDATED:
                self.viewComponent.deSelect()
                self.viewComponent.updateUserGrid(self.userProxy.getUsers())
            
            elif noteName == EmployeeAdmin.AppFacade.USER_ADDED:
                self.viewComponent.deSelect()
                self.viewComponent.updateUserGrid(self.userProxy.getUsers())
            
            elif noteName == EmployeeAdmin.AppFacade.USER_DELETED:
                self.viewComponent.deSelect()
                self.viewComponent.updateUserGrid(self.userProxy.getUsers())
        except:
            raise
            
    def onSelectUser(self, evt):
        self.sendNotification(EmployeeAdmin.AppFacade.USER_SELECTED,self.viewComponent.selectedUser)
    
    def onNewUser(self, evnt):
        self.viewComponent.deSelect()
        self.sendNotification(EmployeeAdmin.AppFacade.NEW_USER)

    def onDeleteUser(self, evnt):
        if self.viewComponent.selectedUser:
            self.sendNotification(EmployeeAdmin.AppFacade.DELETE_USER,self.viewComponent.selectedUser)
            self.viewComponent.deSelect()


class RolePanelMediator(puremvc.patterns.mediator.Mediator, puremvc.interfaces.IMediator):

    NAME = 'RolePanelMediator'
    
    roleProxy = None

    def __init__(self, viewComponent):
        super(RolePanelMediator, self).__init__(RolePanelMediator.NAME, viewComponent)
        self.viewComponent.addBtn.addClickListener(self.onAddRole)
        self.viewComponent.removeBtn.addClickListener(self.onRemoveRole)

        self.roleProxy = self.facade.retrieveProxy(model.RoleProxy.NAME)
        self.viewComponent.updateRoleCombo(consts.RoleList, consts.ROLE_NONE_SELECTED)
        
    def getRolePanel(self):
        return viewComponent
    
    def onAddRole(self, evnt):
        self.roleProxy.addRoleToUser(self.viewComponent.user, self.viewComponent.selectedRole)

    def onRemoveRole(self, evnt):
        self.roleProxy.removeRoleFromUser(self.viewComponent.user, self.viewComponent.selectedRole)
        self.viewComponent.updateRoleList(self.roleProxy.getUserRoles(self.viewComponent.user.username))

    def listNotificationInterests(self):
        return [
        EmployeeAdmin.AppFacade.NEW_USER,
        EmployeeAdmin.AppFacade.USER_ADDED,
        EmployeeAdmin.AppFacade.USER_UPDATED,
        EmployeeAdmin.AppFacade.USER_DELETED,
        EmployeeAdmin.AppFacade.CANCEL_SELECTED,
        EmployeeAdmin.AppFacade.USER_SELECTED,
        EmployeeAdmin.AppFacade.ADD_ROLE_RESULT,
        ]

    def handleNotification(self, note): 
        try:
            noteName = note.getName()   

            if noteName ==  EmployeeAdmin.AppFacade.NEW_USER:
                self.clearForm()

            elif noteName ==  EmployeeAdmin.AppFacade.USER_ADDED:
                self.viewComponent.user = note.getBody()
                roleVO = vo.RoleVO(self.viewComponent.user.username)
                self.roleProxy.addItem(roleVO)
                self.clearForm()

            elif noteName ==  EmployeeAdmin.AppFacade.USER_UPDATED:
                self.clearForm()

            elif noteName ==  EmployeeAdmin.AppFacade.USER_DELETED:
                self.clearForm()

            elif noteName ==  EmployeeAdmin.AppFacade.CANCEL_SELECTED:
                self.clearForm()

            elif noteName ==  EmployeeAdmin.AppFacade.USER_SELECTED:
                self.viewComponent.user = note.getBody()
                if not self.viewComponent.user:
                    self.viewComponent.updateRoleList(self.roleProxy.getUserRoles(None))
                else:
                    self.viewComponent.updateRoleList(self.roleProxy.getUserRoles(self.viewComponent.user.username))

            elif noteName ==  EmployeeAdmin.AppFacade.ADD_ROLE_RESULT:
                self.viewComponent.updateRoleList(self.roleProxy.getUserRoles(self.viewComponent.user.username))
        except:
            raise
        
    def clearForm(self):   
        self.viewComponent.user = None
        self.viewComponent.updateRoleList([])
        self.viewComponent.roleCombo.setItemTextSelection(None)
