<<<<<<< HEAD
import { Routes } from '@angular/router';
import { Register } from './pages/register/register';
import { Login } from './pages/login/login';
import { Dashboard } from './pages/dashboard/dashboard';
=======
import {
  Routes
} from '@angular/router';

import {
  Login
} from './pages/login/login';

import {
  Register
} from './pages/register/register';

import {
  Dashboard
} from './pages/dashboard/dashboard';

import {
  authGuard
} from './guards/auth-guard';

>>>>>>> 4a2f7bf6af4089adac83e10c3f27888ef71c21a8

export const routes: Routes = [

  {
    path: '',
    redirectTo: 'login',
    pathMatch: 'full'
  },

  {
    path: 'login',
    component: Login
  },

  {
    path: 'register',
    component: Register
  },

  {
<<<<<<< HEAD
    path: 'login',
    component: Login
  },
  {
  path: 'dashboard',
  component: Dashboard
}
=======
    path: 'dashboard',
    component: Dashboard,
    canActivate: [authGuard]
  },

  {
    path: '**',
    redirectTo: 'login'
  }

>>>>>>> 4a2f7bf6af4089adac83e10c3f27888ef71c21a8
];