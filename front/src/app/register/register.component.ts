import { Component, OnInit } from '@angular/core';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';
import { AppService } from '../app.service';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent implements OnInit {

  public _form: FormGroup;
  private empty = [];

  constructor(
    private _service: AppService,
    private _builder: FormBuilder
  ) {
    this._form = this._builder.group({
      first_name: [null],
      last_name: [null],
      username: ['', Validators.required],
      password: ['', [Validators.required, Validators.minLength(6)]],
      confirmPassword: ['', Validators.required],
      image: ['0'],
      builds: [this.empty],
      email: ['', [Validators.required, Validators.email]],
      language: ['en'],
      created_at: Date.now(),
      role: 0
    }, { validators: MustMatch('password', 'confirmPassword') });
  }

  ngOnInit() {
  }

  status() { return this._service.getLogin(); }
  id() { return this._service.getId(); }

  setLang(lang: string) {
    console.log('selected:', lang);
  }

  onSubmit() {
    if (this._form.invalid) {
      const invalid = [];
      const controls = this._form.controls;
      for (const name in controls) {
        if (controls[name].invalid) { invalid.push(name); }
      }
      alert(`Invalid Form\n${invalid.join(', ')}`);
      // console.log(invalid);
      return;
    }
    // console.log(this._form.value);
  }
}


export function MustMatch(controlName: string, matchingControlName: string) {
  return (formGroup: FormGroup) => {
    const control = formGroup.controls[controlName];
    const matchingControl = formGroup.controls[matchingControlName];

    if (matchingControl.errors && !matchingControl.errors.mustMatch) {
      // return if another validator has already found an error on the matchingControl
      return;
    }

    // set error on matchingControl if validation fails
    if (control.value !== matchingControl.value) {
      matchingControl.setErrors({ mustMatch: true });
    } else {
      matchingControl.setErrors(null);
    }
  };
}
