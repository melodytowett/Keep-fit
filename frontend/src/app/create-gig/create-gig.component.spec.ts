import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CreateGigComponent } from './create-gig.component';

describe('CreateGigComponent', () => {
  let component: CreateGigComponent;
  let fixture: ComponentFixture<CreateGigComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ CreateGigComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(CreateGigComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
