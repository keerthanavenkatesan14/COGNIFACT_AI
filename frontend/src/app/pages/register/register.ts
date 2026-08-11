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
  RegisterService
} from '../../services/register.service';


@Component({

  selector: 'app-register',

  standalone: true,

  imports: [
    FormsModule,
    RouterLink,
    NgIf
  ],

  templateUrl: './register.html',

  styleUrl: './register.css'

})


export class Register {

  registerData = {

    company_name: '',

    industry: '',

    city: '',

    state: '',

    full_name: '',

    phone: '',

    email: '',

    password: '',

    confirmPassword: ''

  };


  loading = false;

  errorMessage = '';

  successMessage = '';


  constructor(

    private registerService: RegisterService,

    private router: Router

  ) {}


  register(): void {

    this.errorMessage = '';

    this.successMessage = '';


    // -----------------------------
    // Required field validation
    // -----------------------------

    if (
      !this.registerData.company_name.trim() ||
      !this.registerData.industry ||
      !this.registerData.city.trim() ||
      !this.registerData.state.trim() ||
      !this.registerData.full_name.trim() ||
      !this.registerData.phone.trim() ||
      !this.registerData.email.trim() ||
      !this.registerData.password ||
      !this.registerData.confirmPassword
    ) {

      this.errorMessage =
        'Please fill in all required fields.';

      return;

    }


    // -----------------------------
    // Email validation
    // -----------------------------

    const emailPattern =
      /^[^\s@]+@[^\s@]+\.[^\s@]+$/;


    if (!emailPattern.test(this.registerData.email)) {

      this.errorMessage =
        'Please enter a valid email address.';

      return;

    }


    // -----------------------------
    // Phone validation
    // -----------------------------

    const phonePattern =
      /^[0-9]{10}$/;


    if (!phonePattern.test(this.registerData.phone)) {

      this.errorMessage =
        'Please enter a valid 10-digit phone number.';

      return;

    }


    // -----------------------------
    // Password validation
    // -----------------------------

    if (
      this.registerData.password.length < 8
    ) {

      this.errorMessage =
        'Password must be at least 8 characters.';

      return;

    }


    // -----------------------------
    // Confirm password
    // -----------------------------

    if (
      this.registerData.password !==
      this.registerData.confirmPassword
    ) {

      this.errorMessage =
        'Passwords do not match.';

      return;

    }


    this.loading = true;


    // -----------------------------
    // Data sent to Flask
    // -----------------------------

    const data = {

      company_name:
        this.registerData.company_name.trim(),

      industry:
        this.registerData.industry,

      city:
        this.registerData.city.trim(),

      state:
        this.registerData.state.trim(),

      full_name:
        this.registerData.full_name.trim(),

      phone:
        this.registerData.phone.trim(),

      email:
        this.registerData.email.trim(),

      password:
        this.registerData.password

    };


    // -----------------------------
    // API request
    // -----------------------------

    this.registerService

      .register(data)

      .subscribe({

        next: (response) => {

          this.loading = false;

          this.successMessage =
            'Company account created successfully. Redirecting to login...';


          setTimeout(() => {

            setTimeout(() => {

            this.router.navigate([
            '/login'
          ]);

}, 1200);

          }, 1500);

        },


        error: (error) => {

          this.loading = false;

          this.errorMessage =
            error.error?.message ||
            'Registration failed. Please try again.';

        }

      });

  }

}