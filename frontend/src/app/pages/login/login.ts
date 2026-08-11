import { Component } from '@angular/core';

import {
  FormsModule
} from '@angular/forms';

import {
  Router,
  RouterLink
} from '@angular/router';

import {
  NgIf
} from '@angular/common';

import {
  LoginService
} from '../../services/login.service';


@Component({

  selector: 'app-login',

  standalone: true,

  imports: [
    FormsModule,
    RouterLink,
    NgIf
  ],

  templateUrl: './login.html',

  styleUrl: './login.css'

})


export class Login {

  loginData = {

    email: '',

    password: ''

  };


  loading = false;

  errorMessage = '';


  constructor(

    private loginService: LoginService,

    private router: Router

  ) {}


  login(): void {

    this.errorMessage = '';

    this.loading = true;


    this.loginService
      .login(this.loginData)

      .subscribe({

        next: (response) => {

          localStorage.setItem(
            'token',
            response.token
          );


          localStorage.setItem(
            'user',
            JSON.stringify(
              response.user
            )
          );


          this.router.navigate([
            '/dashboard'
          ]);

        },


        error: (error) => {

          this.loading = false;

          this.errorMessage =
            error.error?.message ||
            'Login failed. Please try again.';

        },


        complete: () => {

          this.loading = false;

        }

      });

  }

}