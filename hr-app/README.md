# HRFlow - HR Management System

A modern HR web application for employee directory management and leave request handling with role-based access control.

## 🚀 Features

### Authentication
- Email/password login with JWT tokens
- Session-based authentication
- Protected routes with automatic redirects

### Employee Directory
- View all employees in a sortable, searchable table
- Filter by name, title, department, or email
- Admin-only CRUD operations (Add, Edit, Delete employees)

### Leave Request System
- Submit leave requests with dates and reason
- Multiple leave types: Vacation, Sick, Personal, Maternity, Paternity, Bereavement
- Status filtering (All, Pending, Approved, Rejected)
- Admin approval/rejection workflow

### Role-Based Access Control
| Feature | Admin | Employee |
|---------|-------|----------|
| View employee directory | ✅ | ✅ |
| Add/Edit/Delete employees | ✅ | ❌ |
| Submit leave requests | ✅ | ✅ |
| View own leave requests | ✅ | ✅ |
| View all leave requests | ✅ | ❌ |
| Approve/Reject requests | ✅ | ❌ |

## 🛠️ Tech Stack

- **Framework**: Next.js 14 (App Router)
- **Database**: PostgreSQL
- **ORM**: Prisma
- **Authentication**: NextAuth.js (Credentials Provider)
- **Styling**: Tailwind CSS
- **UI Components**: Radix UI
- **Password Hashing**: bcryptjs
- **Date Handling**: date-fns

## 📋 Prerequisites

- Node.js 18 or higher
- PostgreSQL database
- npm or yarn

## 🔧 Installation

### 1. Navigate to the HR App directory

```bash
cd hr-app
```

### 2. Install dependencies

```bash
npm install
```

### 3. Set up environment variables

Copy the example environment file and update the values:

```bash
cp .env.example .env
```

Edit `.env` with your configuration:

```env
DATABASE_URL="postgresql://user:password@localhost:5432/hrflow?schema=public"
NEXTAUTH_SECRET="your-secret-key-here"
NEXTAUTH_URL="http://localhost:3000"
```

### 4. Set up the database

Push the schema to your database:

```bash
npm run db:push
```

Seed the database with sample data:

```bash
npm run db:seed
```

### 5. Start the development server

```bash
npm run dev
```

Open [http://localhost:3000](http://localhost:3000) in your browser.

## 🔑 Demo Credentials

After running the seed script, you can log in with:

**Admin Account:**
- Email: `sarah.johnson@company.com`
- Password: `password123`

**Employee Account:**
- Email: `emily.davis@company.com`
- Password: `password123`

## 📁 Project Structure

```
hr-app/
├── app/
│   ├── api/
│   │   ├── auth/[...nextauth]/     # NextAuth.js route
│   │   ├── employees/              # Employee CRUD API
│   │   └── leave-requests/         # Leave request API
│   ├── login/                      # Login page
│   └── dashboard/
│       ├── employees/              # Employee directory page
│       └── leave-requests/         # Leave requests page
├── components/
│   ├── ui/                         # Reusable UI components
│   ├── sidebar.tsx                 # Navigation sidebar
│   ├── employee-dialog.tsx         # Employee form dialog
│   ├── leave-request-dialog.tsx    # Leave request form dialog
│   └── delete-confirm-dialog.tsx   # Delete confirmation dialog
├── lib/
│   ├── db.ts                       # Prisma client
│   ├── auth-options.ts             # NextAuth configuration
│   ├── types.ts                    # TypeScript types
│   └── utils.ts                    # Utility functions
├── prisma/
│   ├── schema.prisma               # Database schema
│   └── seed.ts                     # Seed script
└── types/
    └── next-auth.d.ts              # NextAuth type augmentation
```

## 🔐 Security Features

- Passwords hashed with bcrypt (10 salt rounds)
- Server-side session validation on all protected routes
- Role checks on both client and server
- API routes validate user role before operations
- No sensitive data in client-side storage
- CSRF protection via NextAuth.js

## 📝 Available Scripts

| Script | Description |
|--------|-------------|
| `npm run dev` | Start development server |
| `npm run build` | Build for production |
| `npm run start` | Start production server |
| `npm run lint` | Run ESLint |
| `npm run db:push` | Push Prisma schema to database |
| `npm run db:seed` | Seed database with sample data |
| `npm run db:studio` | Open Prisma Studio |

## 🚀 Deployment

### Vercel (Recommended)

1. Push your code to GitHub
2. Import your repository in Vercel
3. Add environment variables in Vercel dashboard
4. Deploy

### Docker

Coming soon...

## 🐛 Troubleshooting

### Database connection issues
- Ensure PostgreSQL is running
- Verify DATABASE_URL in .env is correct
- Check that the database exists

### Authentication issues
- Ensure NEXTAUTH_SECRET is set
- Verify NEXTAUTH_URL matches your application URL

## 📧 Support

For questions and support, please open an issue in this repository.

---

**Built with Next.js and ❤️**
