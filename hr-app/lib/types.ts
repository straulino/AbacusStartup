import { Role, LeaveStatus, LeaveType } from '@prisma/client'

export type { Role, LeaveStatus, LeaveType }

export interface User {
  id: string
  email: string
  name: string
  title: string
  department: string
  role: Role
  createdAt: Date
  updatedAt: Date
}

export interface LeaveRequest {
  id: string
  userId: string
  startDate: Date
  endDate: Date
  leaveType: LeaveType
  reason: string
  status: LeaveStatus
  createdAt: Date
  updatedAt: Date
  user?: User
}

export interface CreateEmployeeData {
  email: string
  password: string
  name: string
  title: string
  department: string
  role: Role
}

export interface UpdateEmployeeData {
  email?: string
  name?: string
  title?: string
  department?: string
  role?: Role
}

export interface CreateLeaveRequestData {
  startDate: string
  endDate: string
  leaveType: LeaveType
  reason: string
}
