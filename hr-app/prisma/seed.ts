import { PrismaClient, Role, LeaveStatus, LeaveType } from '@prisma/client'
import bcrypt from 'bcryptjs'

const prisma = new PrismaClient()

async function main() {
  console.log('Starting seed...')

  // Clear existing data
  await prisma.leaveRequest.deleteMany()
  await prisma.user.deleteMany()

  const hashedPassword = await bcrypt.hash('password123', 10)

  // Create Admin Users
  const sarah = await prisma.user.create({
    data: {
      email: 'sarah.johnson@company.com',
      password: hashedPassword,
      name: 'Sarah Johnson',
      title: 'HR Manager',
      department: 'Human Resources',
      role: Role.ADMIN,
    },
  })

  const michael = await prisma.user.create({
    data: {
      email: 'michael.chen@company.com',
      password: hashedPassword,
      name: 'Michael Chen',
      title: 'Operations Director',
      department: 'Operations',
      role: Role.ADMIN,
    },
  })

  // Create Employee Users
  const emily = await prisma.user.create({
    data: {
      email: 'emily.davis@company.com',
      password: hashedPassword,
      name: 'Emily Davis',
      title: 'Software Engineer',
      department: 'Engineering',
      role: Role.EMPLOYEE,
    },
  })

  const james = await prisma.user.create({
    data: {
      email: 'james.wilson@company.com',
      password: hashedPassword,
      name: 'James Wilson',
      title: 'Product Manager',
      department: 'Product',
      role: Role.EMPLOYEE,
    },
  })

  const olivia = await prisma.user.create({
    data: {
      email: 'olivia.martinez@company.com',
      password: hashedPassword,
      name: 'Olivia Martinez',
      title: 'UX Designer',
      department: 'Design',
      role: Role.EMPLOYEE,
    },
  })

  const william = await prisma.user.create({
    data: {
      email: 'william.brown@company.com',
      password: hashedPassword,
      name: 'William Brown',
      title: 'Financial Analyst',
      department: 'Finance',
      role: Role.EMPLOYEE,
    },
  })

  const sophia = await prisma.user.create({
    data: {
      email: 'sophia.lee@company.com',
      password: hashedPassword,
      name: 'Sophia Lee',
      title: 'Marketing Specialist',
      department: 'Marketing',
      role: Role.EMPLOYEE,
    },
  })

  const daniel = await prisma.user.create({
    data: {
      email: 'daniel.garcia@company.com',
      password: hashedPassword,
      name: 'Daniel Garcia',
      title: 'Senior Developer',
      department: 'Engineering',
      role: Role.EMPLOYEE,
    },
  })

  const ava = await prisma.user.create({
    data: {
      email: 'ava.thompson@company.com',
      password: hashedPassword,
      name: 'Ava Thompson',
      title: 'Sales Representative',
      department: 'Sales',
      role: Role.EMPLOYEE,
    },
  })

  console.log('Users created successfully')

  // Create Leave Requests
  const today = new Date()
  const nextWeek = new Date(today.getTime() + 7 * 24 * 60 * 60 * 1000)
  const nextMonth = new Date(today.getTime() + 30 * 24 * 60 * 60 * 1000)

  // Pending requests
  await prisma.leaveRequest.create({
    data: {
      userId: emily.id,
      startDate: nextWeek,
      endDate: new Date(nextWeek.getTime() + 5 * 24 * 60 * 60 * 1000),
      leaveType: LeaveType.VACATION,
      reason: 'Family vacation to Hawaii',
      status: LeaveStatus.PENDING,
    },
  })

  await prisma.leaveRequest.create({
    data: {
      userId: james.id,
      startDate: nextMonth,
      endDate: new Date(nextMonth.getTime() + 2 * 24 * 60 * 60 * 1000),
      leaveType: LeaveType.PERSONAL,
      reason: 'Personal matters',
      status: LeaveStatus.PENDING,
    },
  })

  await prisma.leaveRequest.create({
    data: {
      userId: sophia.id,
      startDate: new Date(today.getTime() + 14 * 24 * 60 * 60 * 1000),
      endDate: new Date(today.getTime() + 15 * 24 * 60 * 60 * 1000),
      leaveType: LeaveType.SICK,
      reason: 'Medical appointment',
      status: LeaveStatus.PENDING,
    },
  })

  // Approved requests
  await prisma.leaveRequest.create({
    data: {
      userId: daniel.id,
      startDate: new Date(today.getTime() - 14 * 24 * 60 * 60 * 1000),
      endDate: new Date(today.getTime() - 7 * 24 * 60 * 60 * 1000),
      leaveType: LeaveType.VACATION,
      reason: 'Annual leave',
      status: LeaveStatus.APPROVED,
    },
  })

  await prisma.leaveRequest.create({
    data: {
      userId: olivia.id,
      startDate: new Date(today.getTime() - 30 * 24 * 60 * 60 * 1000),
      endDate: new Date(today.getTime() - 28 * 24 * 60 * 60 * 1000),
      leaveType: LeaveType.BEREAVEMENT,
      reason: 'Family bereavement',
      status: LeaveStatus.APPROVED,
    },
  })

  // Rejected requests
  await prisma.leaveRequest.create({
    data: {
      userId: william.id,
      startDate: new Date(today.getTime() + 3 * 24 * 60 * 60 * 1000),
      endDate: new Date(today.getTime() + 17 * 24 * 60 * 60 * 1000),
      leaveType: LeaveType.VACATION,
      reason: 'Extended vacation',
      status: LeaveStatus.REJECTED,
    },
  })

  await prisma.leaveRequest.create({
    data: {
      userId: ava.id,
      startDate: new Date(today.getTime() - 5 * 24 * 60 * 60 * 1000),
      endDate: new Date(today.getTime() - 3 * 24 * 60 * 60 * 1000),
      leaveType: LeaveType.PERSONAL,
      reason: 'Moving to new apartment',
      status: LeaveStatus.REJECTED,
    },
  })

  console.log('Leave requests created successfully')
  console.log('Seed completed!')
  console.log('')
  console.log('Test credentials:')
  console.log('Admin: sarah.johnson@company.com / password123')
  console.log('Employee: emily.davis@company.com / password123')
}

main()
  .catch((e) => {
    console.error(e)
    process.exit(1)
  })
  .finally(async () => {
    await prisma.$disconnect()
  })
