import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { AppService } from '../app.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  public _form: FormGroup;

  constructor(
    private _service: AppService,
    private _builder: FormBuilder
  ) {
    this._form = this._builder.group({
      username: ['', Validators.required],
      password: ['', Validators.required],
    });
  }

  ngOnInit() {
  }

  status() { return this._service.getLogin(); }
  id() { return this._service.getId(); }

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
